
from GameBoard import *
import socket


#Define our game
gameOne = GameBoard()

#Define constants to connect to server.
HOST = "127.0.0.1"
PORT = 65531

#Define the client socket.
ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def playGameFirstTurn():
    incomingData = ClientSocket.recv(1024).decode()

    if incomingData == "player_number: 1":
        gameOne.SetPlayerMessage("IT'S YOUR TURN!")
        

        
    else:
        gameOne.SetPlayerMessage("OPPONENT'S TURN!")
        gameOne.playerTurn = False
        


#def init_session: Function that intializes socket connection to server.
def init_session():
    ClientSocket.connect((HOST, PORT))
    
    
def main():


   
    #gameOne.gameWindow.after(0, init_session)
    gameOne.gameWindow.after(100, playGameFirstTurn)

    
    gameOne.Start()

    
if __name__ == "__main__":
    main()
