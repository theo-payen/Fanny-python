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

	def hashe_password(self,PASSWORD):
		return str(hashlib.sha256(PASSWORD.encode()).hexdigest())

	def password_check(pwd):
		if re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', pwd):
			return True
		else:
			return False



IP = "127.0.0.1"
PORT = 3401
CLIENT = CLIENT(IP,PORT)



CLIENT.connection()
CLIENT.send(LOGIN + "," + CLIENT.hashe_password(PASSWORD))
MESSAGE_CONNECTION = CLIENT.recv().split(",")
CLIENT.close()
