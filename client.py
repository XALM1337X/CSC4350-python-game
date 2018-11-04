

#Module imports required.
from GameBoard import *
from Global import GlobalClient
from multiprocessing import Process, Pipe
import time

def read_packet():  #  NEITHER OF THESE READ_PACKETS WORK FOR SOME REASON. THIS STUFF ALMOST WORKS.
	receivedData = ""
	byte = ""
	#Iterate byte by byte to determine if we have reached the delimiter.
	while byte != "?":
			receivedData = receivedData + byte
			byte = GlobalClient.ClientSocket.recv(1).decode()

		#return our data from server.
	return receivedData
#Define our game. These values need to be read in from the byte stream.
Game = GameBoard("X", "orange", "O", "green")
#def init_session: Function that intializes socket connection to server.
def init_session():
	head,tail = Pipe()
	#Init game variables.
	GlobalClient.ClientSocket.send("init:,".encode())
	data = read_packet()
	Game.playerToken = data.split(":")[0]
	print(Game.playerToken)
	data = read_packet()
	Game.playerColor = data.split(":")[0]
	print(Game.playerColor)
	data = read_packet()
	Game.opponentToken = data.split(":")[0]
	print(Game.opponentToken)
	data = read_packet()
	Game.opponentColor = data.split(":")[0]
	print(Game.opponentColor)
	Game.GamePipe = tail
	#Notify the player that they are connected to the game.
	Game.SetPlayerMessage("CONNECTED!")
	#p1 = Process(target=playGame, args=(Game,head))
	#p1.start()
	p1 = Process(target=Game.Start(), args=(Game,))
	p1.start()
	p1.join()

def main():
	p1 = Process(target=init_session) #Game.gameWindow.after(0, init_session)
	p1.start()
	p1.join()

if __name__ == "__main__":
	main()
