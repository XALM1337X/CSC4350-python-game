#Module imports required.
from GameBoard import *
import socket


#Define our game. These values need to be read in from the byte stream.
Game = GameBoard("B", "blue", "D", "green")

#Define constants to connect to server.
HOST = "127.0.0.1"
PORT = 65531

#Define the client socket.
ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ClientSocket.connect((HOST, PORT))
ClientSocket.setblocking(0)

INCOMING_DATA = ""
OUTGOING_DATA = ""
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
    #return our data from server.
    return receivedData


#Function will sequentially play the game.
def playGame():

    
    INCOMING_DATA = read_packet()
    
    if "player_one" in INCOMING_DATA:
        Game.playerTurn = True
    elif "player_two" in INCOMING_DATA:
        Game.playerTurn = False

    while "winner" not in INCOMING_DATA:
        Game.Update()

        
        if Game.playerTurn:
            Game.ClearPlayerMessage()
            Game.SetPlayerMessage("IT'S YOUR TURN!")
            
            if Game.GetPlayerRow() != 0 and Game.GetPlayerColumn() != 0:
                OUTGOING_DATA = str(Game.GetPlayerRow())+","+str(Game.GetPlayerColumn())
                ClientSocket.send(OUTGOING_DATA.encode())
                Game.playerTurn = False
                INCOMING_DATA = "winner"

        elif not Game.playerTurn:

                INCOMING_DATA = read_packet()
                while INCOMING_DATA == "":
                    INCOMING_DATA = read_packet()
                    if INCOMING_DATA != "":
                        break
                row_column = INCOMING_DATA.split(",")
                Game.UpdateBoard(int(row_column[0]), int(row_column[1]))
                Game.playerTurn = True


    
#def init_session: Function that intializes socket connection to server.
def init_session():
    
    #Game.playerToken = read_packet()
    #Game.playerColor = read_packet()
    #Game.opponentToken = read_packet()
    #Game.opponentColor = read_packet()

	    
	#Notify the player that they are connected to the game. 
    Game.SetPlayerMessage("CONNECTED!")



def main():


    Game.gameWindow.after(100, init_session)
    Game.gameWindow.after(200, playGame)

	#Start the game.
    Game.Update()

if __name__ == "__main__":
    main()
