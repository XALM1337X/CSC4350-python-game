
#Module imports required.
from GameBoard import *
import socket


#Define our game. These values need to be read in from the byte stream.
Game = GameBoard("X", "orange", "O", "green")

#Define constants to connect to server.
HOST = "127.0.0.1"
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
