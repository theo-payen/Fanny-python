import os

fichier = open('Fic_Nom-Groupe', 'r')
contenu = fichier.readlines()

def get_user(user):
    commande = f"grep '^{user}:' /etc/passwd"
    resultat = os.popen(commande).read()
    if resultat:
        return True
    else:
        return False

def new_user(user):
    os.system(f"useradd -N {user}")

def get_group(group):
    commande = f"grep '^{group}:' /etc/group"
    resultat = os.popen(commande).read()
    if resultat:
        return True
    else:
        return False

def new_group(group):
    os.system(f"groupadd {group}")

def add_group(user,group):
    os.system(f"usermod -aG {group} {user}")



for ligne in contenu:
    elements = ligne.split(":") 
    username = elements[0].strip()
    group = elements[1].strip()

    print(username, group)

    if not get_user(username):
        print ("existe pas on crée l'utilisateur")
        new_user(username)

    if not get_group(group):
        print ('existe pas en crée le groupe')
        new_group(group)

    add_group(username,group)


fichier.close()