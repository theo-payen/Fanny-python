#!/usr/bin/python
from Server import Serveur
import threading

IP = "127.0.0.1"
PORT = 5000


SERVER = Serveur(IP,PORT)
SERVER.start()

threadsClients = []

while True:
	SERVER.accept()
	threadsClients.append(threading.Thread(None, SERVER.Instruction, None, (SERVER.client, SERVER.infosClient, SERVER.server), {}))
	threadsClients[-1].start()


#serveur.close()