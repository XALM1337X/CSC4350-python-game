
#Module imports required.
from GameBoard import *
import socket


#Define our game. These values need to be read in from the byte stream. 
Game = GameBoard("X", "magenta", "O", "orange")

#Define constants to connect to server.
HOST = "127.0.0.1"
PORT = 65531

#Define the client socket.
ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#def read_packet: Function reads in one packet sent from the server. 
def read_packet():

    receivedData = ""
    byte = ""

    #Iterate byte by byte to determine if we have reached the delimiter.
    while byte != "*":
        receivedData = receivedData + byte
        byte = ClientSocket.recv(1).decode()

    #return our data from server.
    return receivedData


#Function will sequentially play the game.        
def playGame():

    #Clear out the current player message.
    Game.ClearPlayerMessage()


#def init_session: Function that intializes socket connection to server.
def init_session():
    ClientSocket.connect((HOST, PORT))
    Game.SetPlayerMessage("CONNECTED!")
    
    

def main():


    Game.gameWindow.after(0, init_session)
    Game.gameWindow.after(100, playGame)

	#Start the game. 
    Game.Start()
    
if __name__ == "__main__":
    main()
