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
		self.sock.listen(5)
		while True:
			client, address = self.sock.accept()
			client.settimeout(10)
			threading.Thread(target = self.listenToClient,args = (client,address)).start()
	def listenToClient(self, client, address):
		size = 8192
		socfile = client.makefile('rw', size)
		while True:
			data = socfile.readline().strip()
			request = data.split(" ")
			if data:
				try:
					file = open(request[1][1:len(request[1])])
					data = file.read()
					socfile.write('HTTP/1.1 200 OK\n\n')
					socfile.write('<html><head></head>')
					socfile.write('<body>')
					socfile.write('<h1>%s</h1>' %(data))
					socfile.write('</body>')
					socfile.write('</html>')
					socfile.flush()
					socfile.close()
					client.shutdown(SHUT_WR)
					client.close()
				except:
					socfile.write('HTTP/1.1 404 Not OK\n\n')
					socfile.flush()
					socfile.close()
			else:
				raise error('Client disconnected')
				client.close()