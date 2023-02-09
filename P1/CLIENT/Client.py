import socket, sys

class CLIENT:
	def __init__(self, IP, PORT):
		self.IP = IP
		self.PORT = PORT

	def connection(self):
		try:
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



IP = "127.0.0.1"
PORT = 6000
CLIENT = CLIENT(IP,PORT)

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
	print("---Tools menu---")
	print(" ∘1.get_cpu")
	print(" ∘2.get_memory")
	print(" ∘3.get_process")
	print(" ∘4.get_disk_size")
	print(" ∘5.get_date")
	print(" ∘9.exit")
	print("--------------")
	print("")


	try:
		select_menu = int(input("Select your option -> "))
	except(ValueError):
		print("invalide saisir un nombre")
		continue
	match select_menu:
		case 1:
			CLIENT.send("GET_CPU")
		case 2:
			CLIENT.send("GET_MEMORY")
		case 3:
			CLIENT.send("GET_PROCESS")
			while True:
				MESSAGE_PROCESS = CLIENT.recv().split(",")
				print(MESSAGE_PROCESS[0])
				if MESSAGE_PROCESS[0] == "END_PROCESS":
					break
				print (MESSAGE_PROCESS[0])
				print (MESSAGE_PROCESS[1])
				print (MESSAGE_PROCESS[2])
				print ("________________")
				CLIENT.send("NEXT")
			continue
		case 4:
			CLIENT.send("GET_DISQUE_SIZE")
		case 5:
			CLIENT.send("GET_DATE")
		case 9:
			CLIENT.send("EXIT")
			break
		case _:
			print("Invalide")
			continue
	
	MESSAGE_RETURN = CLIENT.recv().split(",")
	for MESSAGE in MESSAGE_RETURN:
		print (MESSAGE)
	#print(MESSAGE_RETURN_PROCESS[0])

CLIENT.close()
