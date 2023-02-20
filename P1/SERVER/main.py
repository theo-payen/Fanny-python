#!/usr/bin/python
from server import SERVER
import threading

IP = "127.0.0.1"
PORT = 6000

SERVER = SERVER(IP,PORT)
SERVER.start()

threadsClients = []

while True:
    SERVER.accept()
    threadsClients.append(threading.Thread(None, SERVER.Instruction, None, (SERVER.client, SERVER.infosClient, SERVER.server), {}))
    threadsClients[-1].start()


#serveur.close()