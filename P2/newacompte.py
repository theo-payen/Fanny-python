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
    os.system(f"useradd {user}")

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
    print()
    print()
    print(username, group)
    print (get_user(username))
    print (get_group(username))


    
    if not get_user(username):
        print ("existe pas on crée l'utilisateur")
        new_user(username)

    if not get_group(group):
        print ('existe pas en crée le groupe')
        new_group(group)

    #add_group(username,group)
    
    
    
        #groupe existe pas



fichier.close()
# * recupere dans le fichier Fic_Nom-Groupe le non d'utilisateur et le groupe ligne par ligne
# * verifie si l'utilisateur existe deja dans le fichier /etc/passwd

# * verifie si le groupe existe deja dans le fichier /etc/passwd

#si il exite passe 

#si il existe pas on crée l'utilisateur
#os.system("useradd")
#os.system(" groupadd")

#Vérifie l’absence du user dans le fichier /etc/passwd


#Vérifie l’absence du groupe dans le fichier /etc/group avant d’exécuter depuis Python un
#groupadd
