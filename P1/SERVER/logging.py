#!/usr/bin/python
from datetime import datetime

class LOGGING():
    def __init__(self,FILE_LOG):
        self.FILE_LOG = FILE_LOG
        self.right = "a+"

    # Fonction d'ouverture du fichier de logs
    def open(self):
        self.FILE = open(self.FILE_LOG,self.right) 

    # Fonction de fermeture du fichier de logs
    def close(self):
        self.FILE.close()

    # Fonction de récupération de la date et de l'heure au moment T
    def Getdate(self):
        return f'{datetime.now():%m/%d/%Y %H:%M:%S}'

    # Fonction d'écriture dans le fichier de logs
    def print(self,msg,status):
        # Appel de la fonction open pour ouvrir le fichier de logs
        self.open()
        # Stockage du message dans une variable
        # Le format du message est : horodatage (appel fonction Getdate), statut et message 
        Message = self.Getdate(),status,msg
        # Ecriture du message dans le fichier de logs de type string, puis retour à la ligne
        self.FILE.write(str(Message) + "\n")
        # Affichage du message à l'écran
        print(Message)
        # Appel de la fonction close pour fermer le fichier de logs
        self.close()

    # Fonctions stockant chacune un msg différent selon la gravitié de l'évènement

    def info(self,msg):
        self.print(msg,"INFO")

    def warning(self,msg):
        self.print(msg,"WARNING")

    def error(self,msg):
        self.print(msg,"ERROR")

    def critical(self,msg):
        self.print(msg,"CRITICAL")

    def debug(self,msg):
        self.print(msg,"DEBUG")


if __name__ == '__main__':
    print ("veillez importer le script")
else:
    print ("Le script log a été importer avec succès")
