from socket import *
import threading
from state import StateOfGame
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
			client.settimeout(10)
			hostname,hostport = client.getpeername()
			self.sog.playerIPs.append(hostname)
			threading.Thread(target = self.listenToClient,args = (client,address)).start()
	def listenToClient(self, client, address):
		size = 4096
		while True:
			data = client.recv(size)
			strdata = data.decode()
			strdata = strdata + hostname + self.sog.playerIPs
			if data:
				try:
					client.send(strdata.encode())
					client.close()
				except:
					client.send("HTTP/1.1 404 Not OK\n\n").encode()
					client.close()
			else:
				raise error('Client disconnected')
				client.close()
			break
