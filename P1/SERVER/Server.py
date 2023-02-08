#!/usr/bin/python

from tools import TOOLS
from logging import LOGGING

import socket, sys, os


class SERVER():
	def __init__(self,IP,PORT):
		self.IP = IP
		self.PORT = PORT

		self.TOKEN = "uN58tUnC9iQz7Z3u8sGE4GzaqTS562"
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
		self.logging.info("Démarrage des threads pour le client " + adresseIP + " : " + str(port))


		MESSAGE = self.recv().split(",")
		RECV_TOKEN = MESSAGE[0]

		if (RECV_TOKEN != self.TOKEN):
			self.send("REFUSE")
			self.close()
			sys.exit("REFUSE l'autentification")

		print("APPROUVE")
		self.send("APPROUVE")

		while True:
			MESSAGE = self.recv().split(",")
			RECV_ACTION = str(MESSAGE[0])
			match RECV_ACTION:
				case "GET_CPU":
					RETURN_ACTION = self.TOOLS.get_cpu()
				case "GET_MEMORY":
					RETURN_ACTION = self.TOOLS.get_memory()

				case "EXIT":
					print("Exit")
					break
				case _:
					print("Error")
					break
			del RECV_ACTION
			self.send(RETURN_ACTION)

		self.close()


if __name__ == '__main__':
	print ("Veuillez importer le script")
else:
	print ("Le script serveur a été importé avec succès")



