<<<<<<< HEAD

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
##
=======
from socket import *
import threading
class ThreadedServer(object):
	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.sock = socket(AF_INET, SOCK_STREAM)
		self.sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
		self.sock.bind((self.host, self.port))
	def listen(self):
		self.sock.listen(2)
		while True:
			client, address = self.sock.accept()
			client.settimeout(10)
			threading.Thread(target = self.listenToClient,args = (client,address)).start()
	def listenToClient(self, client, address):
		size = 4096
		while True:
                    data = client.recv(size)
                    strdata = data.decode('utf-8')
                    if data:
                        try:
                            client.send(strdata.encode('utf-8'))
                            client.close()
                        except:
                            client.send("HTTP/1.1 404 Not OK\n\n").encode('utf-8')
                            client.close()
                    else:
                        raise error('Client disconnected')
                        client.close()
                    break
>>>>>>> 4627c6cf9ffc8b68b29b0d4892a09909ce756f58
