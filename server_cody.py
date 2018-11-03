
import socket
host = "127.0.0.1"
port=65531

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.bind((host,port))

def read_packet():

    receivedData = ""
    byte = ""

    #Iterate byte by byte to determine if we have reached the delimiter.
    while byte != "?":
        receivedData = receivedData + byte
        byte = mysocket.recv(1).decode()
        print(byte)

    #return our data from server.
    return receivedData

def main():



    ReservedSpots = []

    incomingData = ""
    outgoingData = ""

    
    mysocket.listen(1)


    while True: 
        #Send out first player to connection.
        playerOneConnection, playerOneAddress = mysocket.accept()

        print("Player One Connected...")
        message = "X?magenta?O?orange?"
        playerOneConnection.send(message.encode())

        message = "player_one?"
        playerOneConnection.send(message.encode())


        incoming = playerOneConnection.recv(20)
        print("YOU HAVE RECEIVED THE FOLLOWING MESSAGE: ", incoming)

        print("I AM NOW SENDING THIS MESSSAGE BACK!")
        message = "I AM NOW SENDING THIS MESSAGE BACK!?"
        playerOneConnection.send(message.encode())

        new_message = "MIKE'S MESSAGE!!!!!?"
        playerOneConnection.send(new_message.encode())

        while winnerFunc is false:

            
        

        
        #playerOneConnection.close()
        



if __name__ == "__main__":
    main()
##
