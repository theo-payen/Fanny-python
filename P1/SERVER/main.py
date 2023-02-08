#!/usr/bin/python
from Server import Serveur
import threading

IP = "127.0.0.1"
PORT = 3401


SERVER = Serveur(IP,PORT,DATA_BASE)
SERVER.start()

threadsClients = []

while True:
	SERVER.accept()
	threadsClients.append(threading.Thread(None, SERVER.Instruction, None, (SERVER.client, SERVER.infosClient, SERVER.server), {}))
	threadsClients[-1].start()


#serveur.close()