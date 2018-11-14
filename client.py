#Module imports required.
from GameBoard import *
import socket


#Define our game. These values need to be read in from the byte stream.
Game = GameBoard("X", "green", "O", "blue")

#Define constants to connect to server.
HOST = "143.60.76.32"
PORT = 61002

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
    IS_END = False

    #Read initial packet to determine if we are player one or player two.
    INCOMING_DATA = read_packet()
    
    if "player_one" in INCOMING_DATA:
        Game.playerTurn = True
    elif "player_two" in INCOMING_DATA:
        Game.playerTurn = False
        
    
    while not IS_END:
        Game.Update()
        INCOMING_DATA = read_packet()
        if "winner" in INCOMING_DATA or "tie" in INCOMING_DATA:
            IS_END = True
            Game.playerTurn = False
            break
        
        if Game.playerTurn and not IS_END:
            Game.SetPlayerMessage("IT'S YOUR TURN!")
            
            if Game.GetPlayerRow() != 0 and Game.GetPlayerColumn() != 0:
                OUTGOING_DATA = str(Game.GetPlayerRow())+","+str(Game.GetPlayerColumn())+"?"
                ClientSocket.send(OUTGOING_DATA.encode())
                Game.SetPlayerRowColumn()
                Game.ClearPlayerMessage()
                Game.playerTurn = False
                


        elif not Game.playerTurn and not IS_END:
                
                INCOMING_DATA = read_packet()

                while INCOMING_DATA == "":
                    INCOMING_DATA = read_packet()
                    
                if "winner" in INCOMING_DATA or "tie" in INCOMING_DATA:
                    IS_END = True
                    Game.playerTurn = False                    
                    break
                else:
                    row_column = INCOMING_DATA.split(",")
                    Game.UpdateBoard(int(row_column[0]), int(row_column[1]))
                    Game.playerTurn = True


    #Determine if we are actually a winner.
    if "winner" in INCOMING_DATA:
        is_win = INCOMING_DATA.split(": ")[1].split(",")[0]
        typeOfWin = INCOMING_DATA.split(": ")[1].split(",")[1]

        if is_win == "1":
            Game.ClearPlayerMessage()
            Game.SetPlayerMessage("WINNER!\nPlease Select Quit.")
        else:
            Game.ClearPlayerMessage()
            Game.SetPlayerMessage("YOU LOSE!\nPlease Select Quit.")
        
        Game.DrawWinner(typeOfWin)

    elif "tie" in INCOMING_DATA:
        Game.ClearPlayerMessage()
        Game.SetPlayerMessage("TIE!\nPlease Select Quit.")
        

    ClientSocket.close()
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
    Game.gameWindow.after(1000, playGame)

    #Start the game.
    Game.Start()

if __name__ == "__main__":
    main()
