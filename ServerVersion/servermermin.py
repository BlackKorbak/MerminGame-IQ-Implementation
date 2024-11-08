# Petite importation, on est sur un système d'encapsulation.

from Tests.mermingame import Game

# Importation des sockets

import socket

# Importation des threads pour améliorer ce code

import threading

# Definition du protocole de communication

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0',5555))
server_socket.listen()

print("Ecoute sur le port 5555...")

def play_game(client):
    game = Game()
    with open('gamestart.txt', 'r') as file:
            file_contents = file.read()

            client.sendall(file_contents.encode('utf-8'))

    question = "Votre choix : "

    ask = True

    while ask :

        ask = False

        client.sendall(question.encode('utf-8'))
        
        rep = client.recv(1024).decode()
        rep = rep.lower().strip()

        if rep == "alice":
            player = 1
        elif rep == "bob" :
            player = 2
        else :
            answ = "C'est Alice ou Bob !\n"
            client.sendall(answ.encode('utf-8'))
            ask = True
    
    ask = True

    with open('gamerules.txt', 'r') as file:
            file_contents = file.read()

            client.sendall(file_contents.encode('utf-8'))

    while ask :
        rep = client.recv(1024).decode()
        rep = rep.lower().strip()

        if rep == "help":
             with open('gamerules.txt', 'r') as file:
                file_contents = file.read()

                client.sendall(file_contents.encode('utf-8'))
        elif rep == "circuitry" :
            answ = game.showCircuit()
            client.sendall(answ)
        elif rep == "Measure" :
            answ = "Au revoir !\n"
            client.sendall(answ.encode('utf-8'))
            ask = False
        else :
            answ = "Commande inconnue\n"
            client.sendall(answ.encode('utf-8'))
    

    

def handle_client(client) :

    with open('accueil.txt', 'r') as file:
            file_contents = file.read()

            client.sendall(file_contents.encode('utf-8'))

    with open('aide.txt', 'r') as file:
        file_contents = file.read()

        client.sendall(file_contents.encode('utf-8'))

    ask = True

    while ask :

        rep = client.recv(1024).decode()
        rep = rep.lower().strip()

        if rep == "help":
             with open('aide.txt', 'r') as file:
                file_contents = file.read()

                client.sendall(file_contents.encode('utf-8'))
        elif rep == "ping" :
            answ = "Pong !\n"
            client.sendall(answ.encode('utf-8'))
        elif rep == "quit" :
            answ = "Au revoir !\n"
            client.sendall(answ.encode('utf-8'))
            ask = False
        elif rep == "newgame" :
            play_game(client)
            answ = "Retour au menu principal\n"
            client.sendall(answ.encode('utf-8'))
        else :
            answ = "Commande inconnue\n"
            client.sendall(answ.encode('utf-8'))
    client.close()


try:
    while True:

        # Ecoute + stockage de l'adresse

        client_socket, addr = server_socket.accept()

        print(f"Connection depuis {addr} établie")

        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()
    
except KeyboardInterrupt:
    print("Fermeture de la socket.")

except :
    print("Une erreur est survenue")

finally:
    server_socket.close()


