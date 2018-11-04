import socket

class GlobalClient:
	def __init__(self):
	#Define constants to connect to server.
		self.HOST = "10.0.0.144"#"143.60.76.32"
		self.PORT = 61001
		#Define the client socket.
		self.ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.ClientSocket.connect((self.HOST, self.PORT))
		self.SpotQueryResult =""

GlobalClient = GlobalClient()
