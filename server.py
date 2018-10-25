
import socket


def main():

    host = "127.0.0.1"
    port=65531

    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.bind((host,port))

    ReservedSpots = []

    incomingData = ""
    outgoingData = ""

    
    mysocket.listen(1)


    while True: 
        #Send out first player to connection.
        playerOneConnection, playerOneAddress = mysocket.accept()
        print("Player One Connected...")
        message = "player_number: 1"
        playerOneConnection.send(message.encode())
    
        #Send out second player to connection.
        playerTwoConnection, playerTwoAddress = mysocket.accept()
        message = "player_number: 2"
        playerTwoConnection.send(message.encode())

        #Decode First Selection from client.
        incomingData = playerOneConnection.recv(1024).decode().split(",")

        #Save it in our array, so we can check for a win and send selection
        #back out to the other client. 
        ReservedSpots.append((incomingData[0], incomingData[2]))

      
    print(ReservedSpots)

if __name__ == "__main__":
    main()

