#!/usr/bin/python

from tools import TOOLS
from logging import LOGGING

import socket, sys, os


class SERVER():
	def __init__(self,IP,PORT):
		self.IP = IP
		self.PORT = PORT

		self.ID_client = 0
		self.infosocket = {"ID":[],"SOCKET":[]}
		# FILE LOG
		self.FILE_LOG = "Folder_log/server.log"
		self.logging = LOGGING(self.FILE_LOG)
		# TOOLS
		self.TOOLS = TOOLS()

	def start(self):
		try:
			self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.server.bind((self.IP, self.PORT))
			self.server.listen(5)
		except:
			self.logging.error("Impossible de démarrer le serveur")
			sys.exit()
		else:
			self.logging.info("Serveur démarré")

	def accept(self):
		try:
			self.client,self.infosClient = self.server.accept()
		except:
			self.logging.error("Impossible d'établir la connexion avec le client")
			sys.exit()
		else:
			self.ID_client = self.ID_client + 1
			self.infosocket["ID"].append(self.ID_client)
			self.infosocket["SOCKET"].append(self.client)

	def closeServer(self):
		self.server.close()

	def recv(self):
		try:
			rep = self.client.recv(255)
			return rep.decode()
		except:
			self.logging.error("Impossible de recevoir le message")
			self.close()

	def send(self,msg):
		try:
			msg = msg.encode()
			self.client.send(msg)
		except : 
			self.logging.error("Impossible d'envoyer un message")
			self.close()

	def close(self):
		try:
			self.client.close()
		except:
			self.logging.error("Impossible de fermer la connexion avec le client")
			sys.exit()

	def Instruction(self,client, infosClient, server):   
		adresseIP = infosClient[0]
		port = str(infosClient[1])
		self.logging.info("Démarrage des threads pour le client " + adresseIP + " : " +str(port))

		MESSAGE = self.recv().split(",")
		self.RECV_LOGIN = MESSAGE[0]
		
		self.send("APPROUVE")
		


if __name__ == '__main__':
	print ("Veuillez importer le script")
else:
	print ("Le script serveur a été importé avec succès")



#cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')
#mem_usage=$(free -m | awk 'NR==2{printf "%d/%dMB (%.2f%%)\n", $3,$2,$3*100/$2 }')
"""
import psutil

cpu_percent = psutil.cpu_percent()
print (cpu_percent)
mem = psutil.virtual_memory()
mem_percent = mem.percent

print (mem_percent)

"""

