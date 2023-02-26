# Description

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



