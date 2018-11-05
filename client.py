
#Module imports required.
from GameBoard import *
import socket
import time
from multiprocessing import Process


#Define our game. These values need to be read in from the byte stream.
Game = GameBoard("X", "orange", "O", "green")

#Define constants to connect to server.
HOST = "10.0.0.144"#"143.60.76.32"
PORT = 61001

#Define the client socket.
ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ClientSocket.connect((HOST, PORT))
ClientSocket.setblocking(0)
#def read_packet: Function reads in one packet sent from the server.

def read_packet():
	receivedData = ""
	byte = ""
	#Iterate byte by byte to determine if we have reached the delimiter.
	while byte != "?":
		receivedData = receivedData + byte
		try:
			byte = ClientSocket.recv(1).decode()
		except socket.error:
			return ""
	return receivedData
#
#
#Function will sequentially play the game.
def playGame():
	ClientSocket.send("turncheck".encode())
	incomingData = read_packet()
	Game.Update()
	while "winner" not in incomingData:
		incomingData = read_packet()
		Game.Update()
		if "your_turn" in incomingData:
			print("Its your turn.")
			Game.SetPlayerMessage("IT'S YOUR TURN!")
			#Client.Socket.send("poscheck")
			if Game.playerRow != 0 and Game.playerColumn != 0:
				outgoing = "poscheck:"+str(Game.playerRow)+","+str(Game.playerColumn)
				ClientSocket.send(outgoing.encode())
				Game.playerRow =0
				Game.playerColumn =0

		if "not_turn" in incomingData:
			print("its not my turn")
		if "spot_taken" in incomingData:
			Game.SetPlayerMessage("This spot is taken! Try again.")

		if "spot_open" in incomingData:
			Game.reservedSpots.append(Game.playerRow,Game.playerColumn)
			ClientSocket.send(("end_turn:"+str(Game.playerRow)+","+str(Game.playerColumn)).encode())



		ClientSocket.send("turncheck".encode())
		incomingData = read_packet()
		Game.Update()
		time.sleep(.5)
	if "1" in incomingData:
		typeOfWin = incomingData.split(":")[1].split(",")[1]
		Game.ClearPlayerMessage()
		Game.SetPlayerMessage("YOU WIN!")
		DrawWinner(typeOfWin)
	elif "0" in incomingData:
		typeOfWin = incomingData.split(":")[1].split(",")[1]
		Game.ClearPlayerMessage()
		Game.SetPlayerMessage("YOU LOSE!")
		DrawWinner(typeOfWin)



#def init_session: Function that intializes socket connection to server.
def init_session():

	#Init game variables.
	ClientSocket.send("init:,".encode())
	Game.playerToken = read_packet().split(":")[0]
	Game.playerColor = read_packet().split(":")[0]
	Game.opponentToken = read_packet().split(":")[0]
	Game.opponentColor = read_packet().split(":")[0]
	print(Game.playerToken)
	print(Game.playerColor)
	print(Game.opponentToken)
	print(Game.opponentColor)

	#Notify the player that they are connected to the game.
	Game.SetPlayerMessage("CONNECTED!")



def main():

	Game.gameWindow.after(0, init_session)
	p = Process(target=playGame)
	p.start()
	p.join()

if __name__ == "__main__":
	main()
