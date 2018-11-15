#Class that defines a player in the game.


class Player:

    def __init__(self):
        self.playerConnection = ""
        self.playerAddress = ""
        self.isTurn = False
        self.takenSpots = []
        self.isWinner = False
        self.typeOfWin = ""

