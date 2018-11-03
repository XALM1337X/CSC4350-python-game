from socket import *
import threading
from state import StateOfGame
import time
class ThreadedServer(object):
	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.sock = socket(AF_INET, SOCK_STREAM)
		self.sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
		self.sock.bind((self.host, self.port))
		self.sog = StateOfGame()

	def listen(self):
		self.sock.listen(2)
		while True:
			client, address = self.sock.accept()
			print("trigger1")
			client.settimeout(9999)
			tmphost,tmpport = client.getpeername()
			self.sog.playerIPs.append(tmphost)
			threading.Thread(target = self.listenToClient,args = (client,address)).start()
	def listenToClient(self, client, address):
		size = 1024
		while True:
			data = client.recv(size)
			print("trigger2")
			#strdata = data.decode()
			if data:
				print("trigger3")
				client.settimeout(9999)
				try:
					print("trigger4")
					client_data = data.decode()
					msg = client_data.split(":")
					host,port = client.getpeername()
					if "init" in msg:
						print("trigger5")
						if len(self.sog.playerIPs) <=1:
							print("trigger6")
							client.send("X:,".encode())
							client.send("magenta:,".encode())
							client.send("O:,".encode())
							client.send("orange:,".encode())
						else:
							print("trigger7")
							client.send("O:,".encode())
							client.send("orange:,".encode())
							client.send("X:,".encode())
							client.send("magenta:,".encode())
				except:
					client.send("HTTP/1.1 404 Not OK\n\n").encode()
					client.close()
			else:
				#raise error('Client disconnected')
				#client.close()
				#break
				time.sleep(.05)
