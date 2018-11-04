
import socket

HOST = "127.0.0.1"
PORT = 65531
OUTGOING_DATA = ""
INCOMING_DATA = ""

#GAME CONSTANTS
WINNING_PAIRS = [[(1,1), (1,2), (1,3)], [(2,1),(2,2),(2,3)]]
PLAYER_ONE = True
PLAYER_TWO = False

IS_WINNER = False

ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ServerSocket.bind((HOST, PORT))

ServerSocket.listen(1)

def playerOneRead():
    receivedData = ""
    byte = ""

    while byte != "?":
        receivedData = receivedData + byte
        byte = playerOneConnection.recv(1).decode()

    return receivedData


while True:

    playerOneConnection, playerOneAddress = ServerSocket.accept()
    OUTGOING_DATA="player_two?"
    playerOneConnection.send(OUTGOING_DATA.encode())
    
    #playerTwoConnection, playerTwoAddress = ServerSocket.accept()
    #OUTGOING_DATA="player_two?"
    #playerTwoConnection.send(OUTGOING_DATA.encode())
    PLAYER_ONE=False
    w = False
    while not w:
        
        if PLAYER_ONE:
            print("INSIDE OF IF")
            INCOMING_DATA = playerOneConnection.recv(3).decode()
            print("INCOMING: ", INCOMING_DATA)
            PLAYER_ONE=False
            w = True
        else:
            print("ELSE!")
            INCOMING_DATA = "1,1"
            OUTGOING_DATA = INCOMING_DATA+"?"
            playerOneConnection.send(OUTGOING_DATA.encode())
            PLAYER_ONE=True
    
    
