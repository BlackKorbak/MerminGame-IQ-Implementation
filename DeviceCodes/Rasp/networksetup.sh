#!/bin/bash

# Installation du pack des langages avec encodage UTF-8
sudo apt reinstall locales

# Installation des bibliothèques de base python

sudo apt install python-all

# Retrait des warnings

sudo rm /usr/lib/python3.11/EXTERNALLY-MANAGED

# Installation des bibliothèques 

# Qiskit

pip install qiskit

# Simulateurs Qiskit

pip install qiskit_aer

# Compléments Qiskit

pip install qiskit_ibm_runtime

# matplot pour les résultats des simulations

pip install matplotlib

# Les sorties latex potentielles de Qiskit

pip install pylatexenc

# Création du point d'accès

nmcli device wifi hotspot ssid merminrasp password mermin2024 ifname wlan0

# Mettre le hotspot en activation automatique à chaque démarrage

nmcli connection modify hotspot connection.autoconnect yes

# Lancement du hotspot

nmcli connection up Hotspot

