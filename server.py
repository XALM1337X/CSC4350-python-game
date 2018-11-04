from socket import *
import threading
from state import StateOfGame, Player
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
			self.sog.players.append(Player(str(tmphost), str(tmpport), client))
			threading.Thread(target = self.listenToClient,args = (client,address)).start()
	def listenToClient(self, client, address):
		size = 1024
		while True:
			data = client.recv(size)
			#strdata = data.decode()
			if data:
				print("trigger2")
				client.settimeout(9999)
				print("trigger3")
				client_data = data.decode()
				msg = client_data.split(":")
				host,port = client.getpeername()
				if "init" in msg:
					print("trigger4")
					if len(self.sog.players) <=1:
						print("trigger5")
						for i in self.sog.players:
							if i.playerIp == host:
								i.playerIcon ="X"
								i.playerColor="magenta"
								i.playerSocket.send("X:?".encode())
								i.playerSocket.send("magenta:?".encode())
								i.playerSocket.send("O:?".encode())
								i.playerSocket.send("orange:?".encode())
								self.sog.playerTurn = i.playerIp
					else:
						for i in self.sog.players:
							if i.playerIp == host:
								print("trigger6")
								i.playerIcon ="O"
								i.playerColor="orange"
								i.playerSocket.send("O:?".encode())
								i.playerSocket.send("orange:?".encode())
								i.playerSocket.send("X:?".encode())
								i.playerSocket.send("magenta:?".encode())

				if "turncheck" in msg:
					print("Recieved ping from: "+host)
					for ip in self.sog.players:
						if self.sog.playerTurn == ip.playerIp:
							print("It is "+host+"\'s turn")
							ip.playerSocket.send("your_turn:?".encode())
						else:
							ip.playerSocket.send("not_turn:?".encode())

				if "poscheck" in msg:
					data = msg
					print(host+" has checked if position is taken.")
					for spot in self.sog.reservedSpots:
						if spot == data:
							for ip in self.sog.players:
								if self.sog.playerTurn == ip.playerIp:
									ip.playerSocket.send("spot_taken:?".encode())

					for ip in self.sog.players:
						if self.sog.playerTurn == ip.playerIp:
							ip.playerSocket.send("spot_open:?".encode())

				if "end_turn" in msg:
					print(host+" has ended their turn.")
					tmp = msg[1]
					self.sog.reservedSpots.append(tmp)
					for ip in self.sog.players:
						if ip.playerIp != host:
							self.playerTurn = ip.playerIp






			else:
				#raise error('Client disconnected')
				client.close()
				break
				time.sleep(.05)
