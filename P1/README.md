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

socket : pour la communication réseau
threading : pour gérer les connexions avec les clients en parallèle
datetime : pour la gestion des dates et heures
psutil : pour la récupération des informations système (CPU, mémoire, processus, etc.)
