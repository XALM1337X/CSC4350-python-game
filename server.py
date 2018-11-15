import socket
from player import *

#CONSTANTS FOR SOCKET CONFIGURATION
HOST = "143.60.76.32"
PORT = 61002

#CONSTANTS FOR OUR DATA STREAMS.
OUTGOING_DATA = ""
INCOMING_DATA = ""

#Initialize the socket and bind it to the HOST and PORT.
ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ServerSocket.bind((HOST, PORT))


ServerSocket.listen(2)

def read_packet(playerConnection):
    receivedData = ""
    byte = ""

    while byte != "?":
        receivedData = receivedData + byte
        byte = playerConnection.recv(1).decode()

    return receivedData



def IsWinner(playerOne, playerTwo):

    if "1,1"  in playerOne.takenSpots and "1,2" in playerOne.takenSpots and "1,3" in playerOne.takenSpots:
        playerOne.isWinner = True
        playerOne.typeOfWin = "row_one"
    elif "1,1"  in playerTwo.takenSpots and "1,2" in playerTwo.takenSpots and "1,3" in playerTwo.takenSpots:
        playerTwo.isWinner = True
        playerTwo.typeOfWin  = "row_one"



    elif "2,1"  in playerOne.takenSpots and "2,2"  in playerOne.takenSpots and "2,3"  in playerOne.takenSpots:
        playerOne.isWinner = True
        playerOne.typeOfWin= "row_two"

    elif "2,1"  in playerTwo.takenSpots and "2,2"  in playerTwo.takenSpots and "2,3"  in playerTwo.takenSpots:
        playerTwo.isWinner = True
        playerTwo.typeOfWin = "row_two"



    elif "3,1" in playerOne.takenSpots and "3,2" in playerOne.takenSpots and "3,3" in playerOne.takenSpots:
        playerOne.isWinner = True
        playerOne.typeOfWin = "row_three"

    elif "3,1" in playerTwo.takenSpots and "3,2" in playerTwo.takenSpots and "3,3" in playerTwo.takenSpots:
        playerTwo.isWinner = True
        playerTwo.typeOfWin =  "row_three"




    elif "1,1" in playerOne.takenSpots and "2,1" in playerOne.takenSpots and "3,1" in playerOne.takenSpots:
        playerOne.isWinner = True
        playerOne.typeOfWin = "column_one"

    elif "1,1" in playerTwo.takenSpots and "2,1" in playerTwo.takenSpots and "3,1" in playerTwo.takenSpots:
        playerTwo.isWinner = True
        playerTwo.typeOfWin = "column_one"




    elif "1,2" in playerOne.takenSpots and "2,2" in playerOne.takenSpots and "3,2" in playerOne.takenSpots:
        playerOne.isWinner = True
        playerOne.typeOfWin = "column_two"

    elif "1,2" in playerTwo.takenSpots and "2,2" in playerTwo.takenSpots and "3,2" in playerTwo.takenSpots:
        playerTwo.isWinner = True
        playerTwo.typeOfWin = "column_two"




    elif "1,3" in playerOne.takenSpots and "2,3" in playerOne.takenSpots and "3,3" in playerOne.takenSpots:
        playerOne.isWinner = True
        playerOne.typeOfWin  = "column_three"

    elif "1,3" in playerTwo.takenSpots and "2,3" in playerTwo.takenSpots and "3,3" in playerTwo.takenSpots:
        playerTwo.isWinner = True
        playerTwo.typeOfWin ="column_three"




    elif "1,1" in playerOne.takenSpots and "2,2" in playerOne.takenSpots and "3,3" in playerOne.takenSpots:
        playerOne.isWinner = True
        playerOne.typeOfWin =  "diagonal_left"

    elif "1,1" in playerTwo.takenSpots and "2,2" in playerTwo.takenSpots and "3,3" in playerTwo.takenSpots:
        playerTwo.isWinner = True
        playerTwo.typeOfWin =  "diagonal_left"



    elif "1,3" in playerOne.takenSpots and "2,2" in playerOne.takenSpots and "3,1" in playerOne.takenSpots:
        playerOne.isWinner = True
        playerOne.typeOfWin = "diagonal_right"

    elif "1,3" in playerTwo.takenSpots and "2,2" in playerTwo.takenSpots and "3,1" in playerTwo.takenSpots:
        playerTwo.isWinner = True
        playerTwo.typeOfWin =  "diagonal_right"



   



def main():
    playerOne = Player()
    playerTwo = Player()
    
    while True:

        playerOne.playerConnection, playerOne.playerAddress = ServerSocket.accept()
        OUTGOING_DATA ="X?magenta?O?green?"
        playerOne.playerConnection.send(OUTGOING_DATA.encode())

        OUTGOING_DATA="player_one?"
        playerOne.playerConnection.send(OUTGOING_DATA.encode())
        playerOne.IsTurn = True

        playerTwo.playerConnection, playerTwo.playerAddress = ServerSocket.accept()
        OUTGOING_DATA = "O?green?X?magenta?"
        playerTwo.playerConnection.send(OUTGOING_DATA.encode())

        OUTGOING_DATA = "player_two?"
        playerTwo.playerConnection.send(OUTGOING_DATA.encode())
        
        


        

        while not playerOne.isWinner or not playerTwo.isWinner:
            
            if playerOne.isWinner or playerTwo.isWinner:
                 break
            
            elif len(playerOne.takenSpots) + len(playerTwo.takenSpots) == 9:
                 break

            #print("**************", w, "******************")
            if playerOne.IsTurn:
                INCOMING_DATA = read_packet(playerOne.playerConnection)+"?"
                playerTwo.playerConnection.send(INCOMING_DATA.encode())
                move = INCOMING_DATA.split("?")[0]
                playerOne.takenSpots.append((move))
                playerOne.IsTurn = False
                

            else:
                INCOMING_DATA = read_packet(playerTwo.playerConnection)+"?"
                playerOne.playerConnection.send(INCOMING_DATA.encode())             
                move = INCOMING_DATA.split("?")[0]
                playerTwo.takenSpots.append((move))
                playerOne.IsTurn = True
               
               
            IsWinner(playerOne, playerTwo)
                      
            

        if playerOne.isWinner:
            OUTGOING = "winner: 1,"+playerOne.typeOfWin+"?"
            playerOne.playerConnection.send(OUTGOING.encode())
            OUTGOING = "winner: 0,"+playerOne.typeOfWin+"?"
            playerTwo.playerConnection.send(OUTGOING.encode())

        elif playerTwo.isWinner:

            OUTGOING = "winner: 0,"+playerTwo.typeOfWin+"?"
            playerOne.playerConnection.send(OUTGOING.encode())

            OUTGOING = "winner: 1,"+playerTwo.typeOfWin+"?"
            playerTwo.playerConnection.send(OUTGOING.encode())


        else: 
            OUTGOING = "tie?"
            playerOne.playerConnection.send(OUTGOING.encode())
            playerTwo.playerConnection.send(OUTGOING.encode())
    
        print("Winner sent!")

        break    
    ServerSocket.close()
      


if __name__ == "__main__":
    main()

