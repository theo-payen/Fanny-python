# Import de modules de la librairie Python
import socket, sys , argparse



class CLIENT:
	def __init__(self, IP, PORT):
		self.IP = IP
		self.PORT = PORT

	# Fonction de connexion au serveur
	def connection(self):
		try:
			# Création et sauvegarde du socket de famille d'adresse AF_INET et de type SOCK_STREAM
			self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.client.connect((self.IP, self.PORT))
		except (ConnectionRefusedError):
			print ("Impossible d'établir la connexion entre le serveur et le client !")
			print ("Assurez-vous que le serveur est bien démarré")
			sys.exit()
	def encode(self,msg):
		return msg.encode()
	def decode(self,msg):
		return msg.decode()
	def recv(self):
		rep = self.client.recv(255)
		rep = self.decode(rep)
		return rep
	def send(self,msg):
		msg = self.encode(msg)
		self.client.send(msg)
	def close(self):
		self.client.close()

	def ifmessage(self,msg1,msg2):
		if (msg1 == msg2):
			return True
		else:
			return False

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--ip', help='Adresse IP du serveur' , default='127.0.0.1')
parser.add_argument('-p', '--port', type=int, help='Numéro de port du serveur' ,  default=6000)
args = parser.parse_args()
IP = args.ip
PORT = args.port

CLIENT = CLIENT(IP,PORT)

# Sauvegarde du token
TOKEN = "uN58tUnC9iQz7Z3u8sGE4GzaqTS562"

CLIENT.connection()
CLIENT.send(TOKEN)
MESSAGE_AUTHORISATION = CLIENT.recv().split(",")

if (MESSAGE_AUTHORISATION[0] != "APPROUVE"):
	CLIENT.close()
	sys.exit("refuse l'autentification")

print("Autentifier")
while True:
	print("")
	print("- - Toolbox  Menu - -")
	print("1.  Get_cpu")
	print("2.  Get_memory")
	print("3.  Get_process")
	print("4.  Get_disk_size")
	print("5.  Get_date")
	print("0.  Exit")
	print("- - - - - - - - - - -")
	print("")


	try:
		select_menu = int(input("Select your option -> "))
	except(ValueError):
		print("invalide saisir un nombre")
		continue

	if select_menu == 1:
		CLIENT.send("GET_CPU")
	elif select_menu == 2:
		CLIENT.send("GET_MEMORY")
	elif select_menu == 3:
		CLIENT.send("GET_PROCESS")
		while True:
			MESSAGE_PROCESS = CLIENT.recv().split(",")
			if MESSAGE_PROCESS[0] == "END_PROCESS":
				break
			print ('Pid',MESSAGE_PROCESS[0])
			print ('Name',MESSAGE_PROCESS[1])
			print ('CPU Percent',MESSAGE_PROCESS[2])
			print ("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
			CLIENT.send("NEXT")
		continue
	elif select_menu == 4:
		CLIENT.send("GET_DISQUE_SIZE")
	elif select_menu == 5:
		CLIENT.send("GET_DATE")
	elif select_menu == 0:
		CLIENT.send("EXIT")
		break
	else:
		print("Invalide")
		continue

	MESSAGE_RETURN = CLIENT.recv().split(",")
	for MESSAGE in MESSAGE_RETURN:
		print (MESSAGE)
	#print(MESSAGE_RETURN_PROCESS[0])

CLIENT.close()
