#include <WiFiS3.h>
#include <WiFiClient.h>
#include <genieArduino.h>

const char ssid[] = "merminrasp";                                     // le nom du réseau
const char pass[] = "mermin2024";                                     // le mot de passe du réseau
int status = WL_IDLE_STATUS;                                          // l'état de la connexion Wi-Fi
const int port = 5050;                                                // Le port visé
const char host[] = "10.42.0.1";                                      // L'adresse de la raspberry

Genie genie;
WiFiClient client;
#define RESETLINE 4

void setup() {
  // Ouvre la communication terminal
  Serial.begin(9600);    
  Serial1.begin(9600);
  genie.Begin(Serial1);                                              
  randomSeed(analogRead(0));

  pinMode(RESETLINE, OUTPUT);
  digitalWrite(RESETLINE, 1);
  delay(100);

  // Si fonctionnement module
  if (WiFi.status() == WL_NO_MODULE) {
    Serial.println("Communication avec le module WiFi a échoué!");
    // ne continue pas si le module n'est pas présent :
    while (true);
  }

  // Tente de se connecter au réseau Wi-Fi :
  while (status != WL_CONNECTED) {
    Serial.print("Tentative de connexion à ");
    Serial.println(ssid);
    // Lacement de la connexion :
    status = WiFi.begin(ssid, pass);
    // On attends avant de relancer :
    delay(3000);
  }

  Serial.println("Connecté au réseau Wi-Fi");

  Serial.println("Ouverture de la connexion");

  if(!client.connect(host, port)) {
    Serial.println("Erreur de connexion");
    return;
  }

  client.print("Bob");

  Serial.println("Connexion à la socket réussie !");

  digitalWrite(RESETLINE, 0);

  delay(3500);
  genie.AttachEventHandler(myGenieEventHandler);

  Serial.println("Configuration terminée");

  genie.WriteContrast(15);

}

void loop() {
  genie.DoEvents();
}

void myGenieEventHandler(void) {
  genieFrame Event;
  genie.DequeueEvent(&Event);

  if (Event.reportObject.cmd == GENIE_REPORT_EVENT) {
    if (Event.reportObject.object == GENIE_OBJ_IBUTTOND) {
      if (Event.reportObject.index <= 8) {
        Serial.println("Bouton " + String(Event.reportObject.index) + "Appuyé Normal");
        genie.WriteObject(GENIE_OBJ_USER_LED, Event.reportObject.index, true);
        askBit(Event.reportObject.index);
      }
      if (Event.reportObject.index == 11) {
        Serial.println("Bouton " + String(Event.reportObject.index) + "Appuyé Reset");
        genie.WriteObject(GENIE_OBJ_ILED_DIGIT, 0, 0);
        for(int i = 0; i <= 8; ++i) {
          genie.WriteObject(GENIE_OBJ_USER_LED, i, false);
        }
        client.print("reset");
      }
      if (Event.reportObject.index == 12) {
        Serial.println("Bouton " + String(Event.reportObject.index) + "Appuyé Allocnum");
        int rand = random(1,4);
        Serial.println(rand);
        genie.WriteObject(GENIE_OBJ_ILED_DIGIT, 1, rand);
      }
    }
  }

  
}

void askBit(int button) {

  int lin = (button - button % 3) / 3;
  int col = button % 3;

  client.print("(" + String(lin) + "," + String(col) + ")");

  while(!client.available()) {
    delay(1);
  }

  String reponse = client.readStringUntil('\n');
  
  int resp = reponse.toInt();

  genie.WriteObject(GENIE_OBJ_ILED_DIGIT, 0, resp);

}
