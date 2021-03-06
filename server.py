from socket import *
import threading
class ThreadedServer(object):
	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.sock = socket(AF_INET, SOCK_STREAM)
		self.sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
		self.sock.bind((self.host, self.port))
	def listen(self):
		self.sock.listen(2)
		while True:
			client, address = self.sock.accept()
			client.settimeout(10)
			threading.Thread(target = self.listenToClient,args = (client,address)).start()
	def listenToClient(self, client, address):
		size = 4096
		while True:
			data = client.recv(size)
			strdata = data.decode()
			hostname,hostport = client.getpeername()
			strdata = strdata + hostname
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
