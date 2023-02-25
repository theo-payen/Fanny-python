#!/usr/bin/python

# Depuis le fichier logging.py, importer la classe LOGGING
from logging import LOGGING

# Attention, télécharger psutil avant l'exécution des tools
# pip install psutil
# psutil (process and system utilities) est un module de librairie Python pour récupérer des informations sur les
# processus en cours d'exécution et l'utilisation des ressources système matérielles d'une machine

import psutil,datetime,os

class TOOLS():
    def __init__(self) :
        # Stockage de la localisation du fichier de logs
        self.FILE_LOG = "Folder_log/tools.log"
        self.logging = LOGGING(self.FILE_LOG)

    # Fonction retournant le % d'utilisation du CPU
    def get_cpu(self):
        # Stockage de l'information sur le % d'utilisation du CPU dans la variable CPU
        CPU = str(psutil.cpu_percent())
        self.logging.info("Get CPU tools " + CPU )
        return CPU

    # Fonction retournant le % d'utilisation de la mémoire vive
    def get_memory(self):
        # Stockage de l'information sur l'utilisation de la mémoire dans la variable memoire
        memoir = psutil.virtual_memory()
        # Extraction de l'information sur le % de mémoire utilisée
        # depuis la variable memoire dans la variable memoire_percent
        memoir_percent = str(memoir.percent)
        self.logging.info("Get memory tools " + memoir_percent )		
        return memoir_percent

    def get_process(self):
        self.logging.info("Get all process tools ")
        # Création d'un tableau vide destiné à acceuillir les données sur les processus
        tableau_process = []
        # Pour chaque processus, récupération du PID, du nom et du % d'utilisation du CPU par processus
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
            # Ajout des données au tableau
            tableau_process.append(proc.info)
        return tableau_process

    def get_disque_size(self):
        Partition = "/"
        total = os.statvfs(Partition).f_frsize * os.statvfs(Partition).f_blocks
        used = os.statvfs(Partition).f_frsize * (os.statvfs(Partition).f_blocks - os.statvfs(Partition).f_bfree)
        free = os.statvfs(Partition).f_frsize * os.statvfs(Partition).f_bfree
        total = total / 1024 / 1024
        used = used / 1024 / 1024
        free = free / 1024 / 1024
        percent_used = (used / total) * 100
        self.logging.info("Get disque size "+"total" + "," + str(total) + "," + "used" + "," +str(used) + "," + "free" + "," + str(free) + "," + "percent_used" + "," + str(percent_used))
        return "total" + "," + str(total) + "," + "used" + "," +str(used) + "," + "free" + "," + str(free) + "," + "percent_used" + "," + str(percent_used)

    # Fonction de récupération de la date et de l'heure au moment T
    def get_date(self):
        date = datetime.datetime.now()
        date = date.strftime("%d-%m-%Y_%H:%M:%S")
        self.logging.info("Get date "+date)
        return date



if __name__ == '__main__':
    print ("veillez importer le script")
    TOOLS = TOOLS()
    print (TOOLS.get_process())
else:
    print ("Le script tools a été importer avec succès")
