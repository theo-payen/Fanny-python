# Description

Ce projet est un toolbox permettant de récupérer des informations système telles que la consommation CPU, l'utilisation de la mémoire, les processus en cours d'exécution, la taille du disque et la date. Le serveur utilise des sockets pour communiquer avec les clients.
Le serveur peut également enregistrer des informations sur les événements qui se produisent pendant l'exécution dans un fichier journal.

## Prérequis

Le client Python nécessite Python 3.x 

Le module psutil doit être installé. Pour l'installer, vous pouvez utiliser la commande suivante : 

```bash
pip install psutil
```
##Fonctionnalités

Les fonctionalités utilisés dans ce projet sont :

- Récupération de la consommation CPU
- Récupération de l'utilisation de la mémoire
- Récupération des processus en cours d'exécution
- Récupération de la taille du disque
- Récupération de la date et de l'heure
- Authentification du client en utilisant un jeton
- Connexion multiple de clients simultanément

Voici les options disponibles dans le menu 

•	GET_CPU: retourne l'utilisation actuelle du CPU.
•	GET_MEMORY: retourne l'utilisation actuelle de la mémoire.
•	GET_PROCESS: retourne les informations sur tous les processus en cours d'exécution.
•	GET_DISQUE_SIZE: retourne l'espace disque total et l'espace disque utilisé.
•	GET_DATE: retourne la date et l'heure actuelles du système.
•	EXIT: ferme la connexion avec le serveur.

Le serveur enregistre également les événements suivants dans un fichier journal:
•	INFO: événements d'information.
•	WARNING: événements de mise en garde.
•	ERROR: événements d'erreur.
•	CRITICAL: événements critiques.
•	DEBUG: événements de débogage.

##Fichiers
- server.py
Ce fichier contient la classe SERVER qui gère les sockets et les connexions clients. Il contient également des méthodes pour recevoir et envoyer des messages et pour récupérer les informations système à l'aide de la classe TOOLS.
- login.py
Ce fichier contient la classe LOGGING pour l'enregistrement des messages système dans un fichier journal.
- tools.py
Ce fichier contient la classe TOOLS pour récupérer les informations système telles que la consommation CPU, l'utilisation de la mémoire, les processus en cours d'exécution, la taille du disque et la date.




