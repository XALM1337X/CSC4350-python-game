
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
   if "player_one" in incomingData:
        Game.playerTurn = True
		
   elif "player_two" in incomingData:
        Game.playerTurn = False
		
   	
	
   print("INCOMDING: ", incomingData)
   
   while "winner" not in incomingData:
       print("INSIDE OF WHILE")
       incomingData = "winner"
       
       if Game.playerTurn:
           Game.ClearPlayerMessage()
           
           Game.SetPlayerMessage("IT'S YOUR TURN!")
           Game.playerTurn = False
          
          #while Game.playerRow != 0 and game.playerColumn != 0:
           #  outgoing = str(Game.playerRow)+","+str(Game.playerColumn)+"?"
            # ClientSocket.Send(outgoing.encode())
             #Game.playerTurn = False
        
       else:
           incomingData="winner"   
        #  incomingData="winner"
   msg = "THIS IS A TEST?"       
   ClientSocket.send(msg.encode())
   print("RECEIVED: ", read_packet())
   print("RECEIVED: ", read_packet())
   
   #     if Game.playerTurn:
    #        Game.ClearPlayerMessage()
	
     #       Game.SetPlayerMessage("IT'S YOUR TURN!")
     #   imcomingData = "winner"			
	#	    while Game.playerRow != 0 and Game.playerColumn != 0:
     #           outgoing = str(Game.playerRow)+","+str(Game.playerColumn)+"?"
		#		ClientSocket.Send(outgoing.encode())
		#		Game.SetPlayerRowColumn()
			
		#	Game.playerTurn = False
				
		#elif !Game.PlayerTurn:
		#	opponentMove = incomingData.split(":")[1].split(",")
		#	Game.gameWindow.UpdateBoard(int(opponentMove[0]), int(opponentMove[1]))
		#	Game.playerTurn = True
			
		#incomingData = read_packet()
				
	#if "1" is in incomingData:
      #  typeOfWin = incomingData.split(":")[1].split(",")[1]
     #   Game.ClearPlayerMessage()
      #  Game.SetPlayerMessage("YOU WIN!")
      #  DrawWinner(typeOfWin)
        
    #elif "0" is in incomingData:
     #   typeOfWin = incomingData.split(":")[1].split(",")[1]
      #  Game.ClearPlayerMessage()
      #  Game.SetPlayerMessage("YOU LOSE!")
      #  DrawWinner(typeOfWin)
    #print("TEST")
        
#def init_session: Function that intializes socket connection to server.
def init_session():
    
    Game.playerToken = read_packet()
    Game.playerColor = read_packet()
    Game.opponentToken = read_packet()
    Game.opponentColor = read_packet()

	    
	#Notify the player that they are connected to the game. 
    Game.SetPlayerMessage("CONNECTED!")



def main():


    Game.gameWindow.after(100, init_session)
    Game.gameWindow.after(200, playGame)

	#Start the game.
    Game.Start()

if __name__ == "__main__":
    main()
