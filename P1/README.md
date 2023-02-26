# Description

Ce projet est un toolbox permettant de récupérer des informations système telles que la consommation CPU, l'utilisation de la mémoire, les processus en cours d'exécution, la taille du disque et la date. Le serveur utilise des sockets pour communiquer avec les clients.
Le serveur peut également enregistrer des informations sur les événements qui se produisent pendant l'exécution dans un fichier journal.

## Prérequis

Le client Python nécessite Python 3.x 

Le module psutil doit être installé. Pour l'installer, vous pouvez utiliser la commande suivante : 

```bash
pip install psutil
```
Les modules utilisés dans ce projet sont :

- Récupération de la consommation CPU
- Récupération de l'utilisation de la mémoire
- Récupération des processus en cours d'exécution
- Récupération de la taille du disque
- Récupération de la date et de l'heure
- Authentification du client en utilisant un jeton
- Connexion multiple de clients simultanément
