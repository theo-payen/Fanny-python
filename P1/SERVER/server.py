#!/usr/bin/python

# Depuis le fichier tools.py, importer la classe TOOLS
from tools import TOOLS
# Depuis le fichier logging.py, importer la classe LOGGING
from logging import LOGGING

# Import de modules de la librairie Python
import socket, sys, os


class SERVER():
    def __init__(self,IP,PORT):
        # Sauvegarde de l'IP définie dans la variable IP
        self.IP = IP
        # Sauvegarde du port définie dans la variable PORT
        self.PORT = PORT

        # Sauvegarde du token
        self.TOKEN = "uN58tUnC9iQz7Z3u8sGE4GzaqTS562"
        self.ID_client = 0
        self.infosocket = {"ID":[],"SOCKET":[]}
        # Sauvegarde du chemin du fichier de logs
        self.FILE_LOG = "Folder_log/server.log"
        self.logging = LOGGING(self.FILE_LOG)
        # Sauvegarde de la classe TOOLS
        self.TOOLS = TOOLS()

    # Fonction de démarrage du serveur
    def start(self):
        try:
            # Création et sauvegarde du socket de famille d'adresse AF_INET et de type SOCK_STREAM
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Liaison du socket avec l'IP et le port
            self.server.bind((self.IP, self.PORT))
            # Autorise le serveur à accepter jusqu'à 5 connexions
            self.server.listen(5)
        except:
            self.logging.error("Impossible de démarrer le serveur")
            sys.exit()
        else:
            self.logging.info("Serveur démarré")

    # Fonction d'autorisation du serveur
    def accept(self):
        try:
            # Sauvegarde des informations du client et autorisation de la connexion par le socket
            self.client,self.infosClient = self.server.accept()
        except:
            self.logging.error("Impossible d'établir la connexion avec le client")
            sys.exit()
        else:
            self.ID_client = self.ID_client + 1
            self.infosocket["ID"].append(self.ID_client)
            self.infosocket["SOCKET"].append(self.client)

    # Fonction de fermeture de la connexion du  client
    def close_client(self):
        try:
            # Ferme la connexion du serveur au socket du client
            self.client.close()
        except:
            self.logging.error("Impossible de fermer la connexion avec le client")
            sys.exit()

    # Fonction de fermeture de la connexion au serveur
    def close_server(self):
        try:
            # Ferme la connexion du client au socket du serveur
            self.server.close()
        except:
            self.logging.error("Impossible de fermer la connexion avec le server")
            sys.exit()
        

    # Permet de récupérer un message du client
    def recv(self):
        try:
            # Stockage du message du client dans la variable rep (réponse)
            rep = self.client.recv(255)
            # La fonction décode la réponse du client avant de la retourner
            return rep.decode()
        except:
            # En cas d'impossibilité de récupérer la réponse du client, envoi d'un message de log...
            self.logging.error("Impossible de recevoir le message")
            # puis fermeture de la connexion avec le client
            self.close_client()

    # Permet d'envoyer un message au client
    def send(self,msg):
        try:
            # Encodage du message avant l'envoi au client
            msg = msg.encode()
            # Envoi du message au client
            self.client.send(msg)
        except : 
            # En cas d'impossibilité d'envoi du message au client, envoi d'un message de log...
            self.logging.error("Impossible d'envoyer un message")
            # puis fermeture de la connexion avec le client
            self.close_client()

    # Fonction contenant les instructions autorisées au client
    def Instruction(self,client, infosClient, server):   
        client_adresseIP = infosClient[0]
        client_port = str(infosClient[1])
        print_information_client = " " + client_adresseIP + " : " + client_port

        self.logging.info("Démarrage des threads pour le client" + print_information_client)

        MESSAGE = self.recv().split(",")
        RECV_TOKEN = MESSAGE[0]

        # En cas de différence de token, refus de la connexion...
        if (RECV_TOKEN != self.TOKEN):
            # avec notification du client
            self.send("REFUSE" + print_information_client)
            # et fermeture de la connexion avec le client
            self.close_client()
            sys.exit("REFUSE l'autentification")

        # En cas de match du token, acceptation de la connexion...
        self.logging.info("APPROUVE" + print_information_client)
        # avec notification du client
        self.send("APPROUVE")

        while True:
            # Stockage dans la variable MESSAGE du message envoyé par le client
            MESSAGE = self.recv().split(",")
            # Forcage du message envoyé par le client en type string et stockage dans la variable RECV_ACTION
            RECV_ACTION = str(MESSAGE[0])

            # Appel de la classe TOOLS et de ses différentes fonctions selon la demande du client
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