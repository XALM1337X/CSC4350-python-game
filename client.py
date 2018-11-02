
#Module imports required.
from GameBoard import *
import socket


#Define our game. These values need to be read in from the byte stream.
Game = GameBoard("X", "orange", "O", "green")

#Define constants to connect to server.
HOST = "143.60.76.32"
PORT = 61001

#Define the client socket.
ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ClientSocket.connect((HOST, PORT))

#def read_packet: Function reads in one packet sent from the server.
def read_packet():

    receivedData = ""
    byte = ""

    #Iterate byte by byte to determine if we have reached the delimiter.
    while byte != "?":
        receivedData = receivedData + byte
        byte = ClientSocket.recv(1).decode()

    #return our data from server.
    return receivedData


#Function will sequentially play the game.
def playGame():
	
	incomingData = read_packet()
	
	while "winner" is not in incomingData:
		
		if "opponent_turn" is in incomingData:
			Game.ClearPlayerMessage()
			opponentMove = incomingData.split(":")[1].split(",")
			Game.gameWindow.UpdateBoard(int(opponentMove[0]), int(opponentMove[1]))
			Game.playerTurn = True
            
         if Game.playerTurn:
			Game.ClearPlayerMessage()
			Game.SetPlayerMessage("IT'S YOUR TURN!")
			
			while Game.playerRow != 0 and Game.playerColumn != 0:
                outgoing = str(Game.playerRow)+","+str(Game.playerColumn)
				ClientSocket.Send(outgoing.encode())
				Game.SetPlayerRowColumn()
				
		incomingData = read_packet()
				
	if "1" is in incomingData:
        typeOfWin = incomingData.split(":")[1].split(",")[1]
        Game.ClearPlayerMessage()
        Game.SetPlayerMessage("YOU WIN!")
        DrawWinner(typeOfWin)
    elif "0" is in incomingData:
        typeOfWin = incomingData.split(":")[1].split(",")[1]
        Game.ClearPlayerMessage()
        Game.SetPlayerMessage("YOU LOSE!")
        DrawWinner(typeOfWin)
        
        
#def init_session: Function that intializes socket connection to server.
def init_session():

	#Init game variables. 
    Game.playerToken = read_packet()
    Game.playerColor = read_packet()
    Game.opponentToken = read_packet()
    Game.opponentColor = read_packet()
	
	#Notify the player that they are connected to the game. 
    Game.SetPlayerMessage("CONNECTED!")



def main():


    Game.gameWindow.after(0, init_session)
    Game.gameWindow.after(100, playGame)

	#Start the game.
    Game.Start()

if __name__ == "__main__":
    main()
