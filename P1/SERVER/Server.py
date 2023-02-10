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

    def close_client(self):
        try:
            self.client.close()
        except:
            self.logging.error("Impossible de fermer la connexion avec le client")
            sys.exit()

    def close_server(self):
        try:
            self.server.close()
        except:
            self.logging.error("Impossible de fermer la connexion avec le server")
            sys.exit()
        

    def recv(self):
        try:
            rep = self.client.recv(255)
            return rep.decode()
        except:
            self.logging.error("Impossible de recevoir le message")
            self.close_client()

    def send(self,msg):
        try:
            msg = msg.encode()
            self.client.send(msg)
        except : 
            self.logging.error("Impossible d'envoyer un message")
            self.close_client()

    def Instruction(self,client, infosClient, server):   
        client_adresseIP = infosClient[0]
        client_port = str(infosClient[1])
        print_information_client = " " + client_adresseIP + " : " + client_port

        self.logging.info("Démarrage des threads pour le client" + print_information_client)

        MESSAGE = self.recv().split(",")
        RECV_TOKEN = MESSAGE[0]

        if (RECV_TOKEN != self.TOKEN):
            self.send("REFUSE" + print_information_client)
            self.close_client()
            sys.exit("REFUSE l'autentification")

        self.logging.info("APPROUVE" + print_information_client)
        self.send("APPROUVE")

        while True:
            MESSAGE = self.recv().split(",")
            RECV_ACTION = str(MESSAGE[0])

            if RECV_ACTION == "GET_CPU":
                RETURN_ACTION = self.TOOLS.get_cpu()
            elif RECV_ACTION == "GET_MEMORY":
                RETURN_ACTION = self.TOOLS.get_memory()
            elif RECV_ACTION == "GET_PROCESS":
                tab_process = self.TOOLS.get_process()
                for item in tab_process:
                    pid = str((item['pid']))
                    name = str((item['name']))
                    cpu_percent = str((item['cpu_percent']))
                    self.send(pid + "," + name + "," + cpu_percent)
                    self.recv().split(",")
                RETURN_ACTION = "END_PROCESS"
            elif RECV_ACTION == "GET_DISQUE_SIZE":
                RETURN_ACTION = self.TOOLS.get_disque_size()
            elif RECV_ACTION == "GET_DATE":
                RETURN_ACTION = self.TOOLS.get_date()
            elif RECV_ACTION == "EXIT":
                self.logging.info("close client" + print_information_client)
                break
            else:
                print("Error")
                break

            self.send(RETURN_ACTION)

        self.close_client()


if __name__ == '__main__':
    print ("Veuillez importer le script")
else:
    print ("Le script serveur a été importé avec succès")



