# Fanny-python
- projet Fanny 4SRC Python de DEBLANGY

## Sujet 1
## Description

Ce projet est un toolbox permettant de récupérer des informations système telles que la consommation CPU, l'utilisation de la mémoire, les processus en cours d'exécution, la taille du disque et la date. Le serveur utilise des sockets pour communiquer avec les clients.
Le serveur peut également enregistrer des informations sur les événements qui se produisent pendant l'exécution dans un fichier journal.

## Prérequis

Le client Python nécessite Python 3.x 

Le module psutil doit être installé. Pour l'installer, vous pouvez utiliser la commande suivante : 

```bash
pip install psutil
```
## Fonctionnalités

Les fonctionalités utilisés dans ce projet sont :

- Récupération de la consommation CPU
- Récupération de l'utilisation de la mémoire
- Récupération des processus en cours d'exécution
- Récupération de la taille du disque
- Récupération de la date et de l'heure
- Authentification du client en utilisant un jeton
- Connexion multiple de clients simultanément

Voici les options disponibles dans le menu 

-	GET_CPU: retourne l'utilisation actuelle du CPU.
-	GET_MEMORY: retourne l'utilisation actuelle de la mémoire.
-	GET_PROCESS: retourne les informations sur tous les processus en cours d'exécution.
-	GET_DISQUE_SIZE: retourne l'espace disque total et l'espace disque utilisé.
-	GET_DATE: retourne la date et l'heure actuelles du système.
-	EXIT: ferme la connexion avec le serveur.

Le serveur enregistre également les événements suivants dans un fichier journal:
-	INFO: événements d'information.
-	WARNING: événements de mise en garde.
-	ERROR: événements d'erreur.
-	CRITICAL: événements critiques.
-	DEBUG: événements de débogage.

Le fichier journal se trouve dans le répertoire Folder_log/server.log.

## Fichiers
- server.py
Ce fichier contient la classe SERVER qui gère les sockets et les connexions clients. Il contient également des méthodes pour recevoir et envoyer des messages et pour récupérer les informations système à l'aide de la classe TOOLS.
- login.py
Ce fichier contient la classe LOGGING pour l'enregistrement des messages système dans un fichier journal.
- tools.py
Ce fichier contient la classe TOOLS pour récupérer les informations système telles que la consommation CPU, l'utilisation de la mémoire, les processus en cours d'exécution, la taille du disque et la date.
- main.py
Ce fichier contient le code principal pour démarrer le serveur et gérer les connexions clients.


## Utilisation 

1- Exécuter le script "main.py" pour démarrer le serveur ```python3 main.py```

2- Le client Python peut être utilisé en exécutant le script client.py avec les arguments suivants :
-	-i ou --ip : adresse IP du serveur (par défaut 127.0.0.1)
-	-p ou --port : numéro de port du serveur (par défaut 6000)

Exemple d'utilisation : ```python3 client.py -i 192.168.1.100 -p 8000```

3- Modifier l'adresse IP et le port du serveur dans le fichier main.py si nécessaire.









## Sujet 2

## Description

Ce script permet d'ajouter des utilisateurs à des groupes en se basant sur un fichier qui contient la liste des utilisateurs et leurs groupes respectifs.

## Prérequis

Le client Python nécessite Python 3.x 

il nous faut des droits d'administrateur.


## Fichiers
- Fic_Nom-Group :
Créer un fichier contenant une liste de noms d'utilisateur et de noms de groupe séparés par des deux points (:). Chaque utilisateur et groupe doit être sur une ligne séparée. Le nom de l'utilisateur et le nom du groupe ne doivent pas contenir de deux points. 
- Par exemple :

```bash
nom_utilisateur:nom_groupe
nom_utilisateur_2:nom_groupe_2
```

## Utilisation 

1- Exécuter le script "newacompte.py"  ```python3 newacompte.py```



## Fonctions du script

get_user(user)
Cette fonction prend un nom d'utilisateur en tant qu'argument et renvoie True si l'utilisateur existe déjà, sinon False.

new_user(user)
Cette fonction crée un nouvel utilisateur à l'aide de la commande useradd. Elle prend un nom d'utilisateur en tant qu'argument.

get_group(group)
Cette fonction prend un nom de groupe en tant qu'argument et renvoie True si le groupe existe déjà, sinon False.

new_group(group)
Cette fonction crée un nouveau groupe à l'aide de la commande groupadd. Elle prend un nom de groupe en tant qu'argument.

add_group(user, group)
Cette fonction ajoute un utilisateur à un groupe à l'aide de la commande usermod. Elle prend le nom de l'utilisateur et le nom du groupe en tant qu'arguments.



## Repartition des tâches


Projet | Sujet                     | Collaborateur 1 | Collaborateur 2
------ | -------                   | -----           | -------
P1     | `Tools`                   | Maxime          | Mukil 
P1     | `Conection client serveur`| Mohamed         | Théo
P1     | `Logs`                    | Mukil           | Maxime 
P2     | `Script`                  | Théo            | Mohamed 
