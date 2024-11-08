# Petite importation, on est sur un système d'encapsulation.

from mermingame import Game

# Importation des sockets

import socket

# Importation des threads

import threading

# handle_alice / bob (client, game) : Prends une connexion socket client et une instance de jeu mermin en entrée.
#   Lit les requêtes du client sous forme (x,y), et renvoie la mesure de la case x,y

def handle_alice(client) :

    ask = True

    while ask :
        rep = client.recv(1024).decode()
        rep = rep.lower().strip()

        if rep == "quit" :
            ask = False
        if rep == "reset" :
            global game
            game = Game()
        else :
            x_y = rep.strip("()").split(",")
            lin = int(x_y[0])
            col = int(x_y[1])
            
            bit = game.getAliceMeasure(lin, col)
            bit = bit + "\n"
            client.sendall(bit.encode('utf-8'))

def handle_bob(client) :

    ask = True

    while ask :
        rep = client.recv(1024).decode()
        rep = rep.lower().strip()

        if rep == "quit" :
            ask = False
        if rep == "reset" :
            global game
            game = Game()
        else :
            x_y = rep.strip("()").split(",")
            lin = int(x_y[0])
            col = int(x_y[1])
            
            bit = game.getAliceMeasure(lin, col)
            bit = bit + "\n"

            client.sendall(bit.encode('utf-8'))


# handle_client(client, game) : Prends une socket client, et une instance de jeu mermin, et redirige le client vers la fonction associée.

def handle_client(client) :

    rep = client.recv(1024).decode()
    rep = rep.lower().strip()

    print(rep)

    if rep == "alice" :
        handle_alice(client)
    else :
        handle_bob(client)
    
    client.close()



# Definition du protocole de communication

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0',5050))
server_socket.listen()

print("Ecoute sur le port 5050...")

global game 
game = Game()

try:
    while True:

        # Ecoute + stockage de l'adresse

        client_socket, addr = server_socket.accept()

        print(f"Connection depuis {addr} établie")

        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()
    
except KeyboardInterrupt:
    print("Fermeture de la socket.")

except Exception as e:
    print("Une erreur est survenue:", e)
    server_socket.close()

finally:
    server_socket.close()
