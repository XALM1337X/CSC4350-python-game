from server import ThreadedServer

def main():
    #server = ThreadedServer("127.0.0.1", 1337)
    #server.listen()
    server = ThreadedServer("127.0.0.1", 1337).listen()






if __name__ == "__main__":
    main()
