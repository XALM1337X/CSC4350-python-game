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
			msg =""
			data=""
			data = client.recv(size)
			#strdata = data.decode()
			if data:
				#print("trigger2")
				client.settimeout(9999)
				#print("trigger3")
				client_data = data.decode()
				msg = client_data.split(":")
				host,port = client.getpeername()
				if "init" in msg:
					print("trigger4")
					if len(self.sog.players) ==1:
						print("trigger5")
						for i in self.sog.players:
							if i.playerIp == host:
								i.playerIcon ="X"
								i.playerColor="magenta"
								i.playerSocket.send("X:?".encode())
								time.sleep(.5)
								i.playerSocket.send("magenta:?".encode())
								time.sleep(.5)
								i.playerSocket.send("O:?".encode())
								time.sleep(.5)
								i.playerSocket.send("orange:?".encode())
								self.sog.playerTurn = i.playerIp
								i.playerTurn = True
								msg =""
								data=""
					elif len(self.sog.players) > 1:
						for i in self.sog.players:
							if i.playerIp == host:
								print("trigger6")
								i.playerIcon ="O"
								i.playerColor="orange"
								i.playerSocket.send("O:?".encode())
								time.sleep(.5)
								i.playerSocket.send("orange:?".encode())
								time.sleep(.5)
								i.playerSocket.send("X:?".encode())
								time.sleep(.5)
								i.playerSocket.send("magenta:?".encode())
								i.playerTurn = False
								msg =""
								data=""

				if "turncheck" in msg:
					print("Recieved ping from: "+host)
					if self.sog.playerTurn == host:
						print("It is "+host+"\'s turn")
						for ip in self.sog.players:
							if ip.playerIp == host and i.playerTurn:
								ip.playerSocket.send("your_turn:?".encode())
								msg =""
								data=""
					else:
						for ip in self.sog.players:
							if ip.playerIp == host and i.playerTurn == False:
								ip.playerSocket.send("not_turn:?".encode())
								msg =""
								data=""
					msg =""
					data=""

				if "poscheck" in msg:
					data = msg[1]
					print(str(data))
					print(str(host)+" has checked if position: "+str(data)+" is taken.")

					for ip in self.sog.players:
						if "0,0" in data and ip.playerIp == host:
							print("Waiting for decision.")
							ip.playerSocket.send("your_turn:?".encode())
							msg =""
							data=""
						elif data in self.sog.reservedSpots and ip.playerIp == host:
							print("sent: spot_taken.")
							ip.playerSocket.send("spot_taken:?".encode())
							msg =""
							data=""
						elif data not in self.sog.reservedSpots and ip.playerIp == host:
							print("sent: spot_open.")
							ip.playerSocket.send("spot_open:?".encode())
							msg =""
							data=""
					msg =""
					data=""


					#ip.playerSocket.send("spot_taken:?".encode())
					#ip.playerSocket.send("spot_open:?".encode())

				if "end_turn" in msg:
					tmp = msg[1]
					print(str(host)+" has ended their turn with move: "+str(data))
					self.sog.reservedSpots.append(tmp)
					for ip in self.sog.players:
						if ip.playerIp != host and ip.playerTurn == False:
							self.sog.playerTurn = ip.playerIp
							ip.playerTurn = True
							msg =""
							data=""
						if ip.playerIp ==host and ip.playerTurn == True:
							ip.playerTurn =False
							msg =""
							data=""

				msg =""
				data=""
			else:
				#raise error('Client disconnected')
				client.close()
				break
				time.sleep(.05)
