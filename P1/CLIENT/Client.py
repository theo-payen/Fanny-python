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
	print("Tools menu")
	print("1.get_cpu")
	print("2.get_memory")
	print("3.get_process")
	print("9.exit")
	select_menu = int(input("Select your menu:"))
	match select_menu:
		case 1:
			Action = CLIENT.send("GET_CPU")
		case 2:
			Action = CLIENT.send("GET_MEMORY")
		case 3:
			Action = CLIENT.send("GET_PROCESS")
			while True:
				MESSAGE_PROCESS = CLIENT.recv().split(",")
				if MESSAGE_PROCESS[0] == "END_PROCESS":
					break
				CLIENT.send("NEXT")

		case 9:
			Action = "EXIT"
		case _:
			print("Invalide")
			continue

	if Action == "EXIT":
		break
	del Action
	MESSAGE_AUTHORISATION = CLIENT.recv().split(",")
	print(MESSAGE_AUTHORISATION[0])

CLIENT.close()
