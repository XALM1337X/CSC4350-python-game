
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
def IsReserved(tmp):
	if tmp not in Game.ReservedSpots:
		return False
	else:
		return True

#def read_packet: Function reads in one packet sent from the server.
def drawPos(row, column, icon, color):
	Game.ClearPlayerMessage()
	tmp = str(row)+","+str(column)
	if IsReserved(tmp):
		Game.ClearPlayerMessage()
		Game.SetPlayerMessage("SPOT ALREADY TAKEN!\nSELECT AGAIN!")

	else:
		if row == 1 and column == 1:
			Game.SetPosLabel(1,1, icon, color)
			Game.ReservedSpots.append(str(row)+","+str(column))
			print("DATATRIGGER#1")
		elif row == 1 and column == 2:
			Game.SetPosLabel(1,2, icon, color)
			Game.ReservedSpots.append(str(row)+","+str(column))
			print("DATATRIGGER#2")
		elif row == 1 and column == 3:
			Game.SetPosLabel(1,3, icon, color)
			Game.ReservedSpots.append(str(row)+","+str(column))
			print("DATATRIGGER#3")
		elif row == 2 and column == 1:
			Game.SetPosLabel(2,1, icon, color)
			Game.ReservedSpots.append(str(row)+","+str(column))
			print("DATATRIGGER#4")
		elif row == 2 and column == 2:
			Game.SetPosLabel(2,2, icon, color)
			Game.ReservedSpots.append(str(row)+","+str(column))
			print("DATATRIGGER#5")
		elif row == 2 and column == 3:
			Game.SetPosLabel(2,3, icon, color)
			Game.ReservedSpots.append(str(row)+","+str(column))
			print("DATATRIGGER#6")
		elif row == 3 and column == 1:
			Game.SetPosLabel(3,1, icon, color)
			Game.ReservedSpots.append(str(row)+","+str(column))
			print("DATATRIGGER#7")
		elif row == 3 and column == 2:
			Game.SetPosLabel(3,2, icon, color)
			Game.ReservedSpots.append(str(row)+","+str(column))
			print("DATATRIGGER#8")
		elif row == 3 and column == 3:
			Game.SetPosLabel(3,3, icon, color)
			Game.ReservedSpots.append(str(row)+","+str(column))
			print("DATATRIGGER#9")
		Game.canvas.pack()

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
	init_session()
	end_turn_flag=False
	PlayerQuery=""
	ClientSocket.send("turncheck".encode())
	incomingData = read_packet()
	Game.Update()
	while "winner" not in incomingData:
		PlayerQuery =""

		if "your_turn" in incomingData:
			Game.playerTurn = True
			PlayerQuery="poscheck:"
			print("Its your turn:")
			Game.SetPlayerMessage("IT'S YOUR TURN!")
			#Client.Socket.send("poscheck")
			if Game.playerRow != 0 and Game.playerColumn != 0:
				print(str(Game.playerRow)+str(Game.playerColumn))
				PlayerQuery = PlayerQuery+str(Game.playerRow)+","+str(Game.playerColumn)
				incomingData =""
			else:
				print("Waiting on player selection.")
				PlayerQuery = PlayerQuery+"0,0"
				incomingData =""
		if "spot_taken" in incomingData:
			Game.SetPlayerMessage("This spot is taken! Try again.")
			PlayerQuery ="turncheck:"
			incomingData =""
			Game.playerRow =0
			Game.playerColumn =0
		if "spot_open" in incomingData:
			print("spot_open")
			drawPos(Game.playerRow,Game.playerColumn, Game.playerToken, Game.playerColor)
			incomingData =""
			PlayerQuery ="end_turn:"+str(Game.playerRow)+","+str(Game.playerColumn)
			ClientSocket.send(PlayerQuery.encode())
			end_turn_flag = True
			Game.playerTurn == False
			Game.playerRow =0
			Game.playerColumn =0
			time.sleep(5)

		if "not_turn" in incomingData:
			incomingData =""
			Game.playerTurn == False
			Game.playerRow =0
			Game.playerColumn =0
			PlayerQuery ="turncheck:"
			print("its not my turn")





		if Game.playerTurn == False:
			ClientSocket.send("turncheck:".encode())
		else:
			if end_turn_flag == True:
				PlayerQuery ="turncheck:"
				end_turn_flag = False
			ClientSocket.send(PlayerQuery.encode())
		#incomingData = read_packet()
		time.sleep(1.5)
		Game.Update()
		incomingData=""
		incomingData = read_packet()

	#if "1" in incomingData:
	#	typeOfWin = incomingData.split(":")[1].split(",")[1]
	#	Game.ClearPlayerMessage()
	#	Game.SetPlayerMessage("YOU WIN!")
	#	DrawWinner(typeOfWin)
	#elif "0" in incomingData:
	#	typeOfWin = incomingData.split(":")[1].split(",")[1]
	#	Game.ClearPlayerMessage()
	#	Game.SetPlayerMessage("YOU LOSE!")
	#	DrawWinner(typeOfWin)



#def init_session: Function that intializes socket connection to server.
def init_session():

	#Init game variables.
	ClientSocket.send("init:,".encode())
	time.sleep(1)
	Game.playerToken = read_packet().split(":")[0]
	time.sleep(1)
	Game.playerColor = read_packet().split(":")[0]
	time.sleep(1)
	Game.opponentToken = read_packet().split(":")[0]
	time.sleep(1)
	Game.opponentColor = read_packet().split(":")[0]

	print("playerToken: "+Game.playerToken)
	print("playerColor: "+Game.playerColor)
	print("opponentToken: "+Game.opponentToken)
	print("opponentColor: "+Game.opponentColor)

	#Notify the player that they are connected to the game.
	Game.SetPlayerMessage("CONNECTED!")



def main():
	time.sleep(5)
	p = Process(target=playGame)
	p.start()
	p.join()

if __name__ == "__main__":
	main()
