class StateOfGame():
	def __init__(self):
		self.playerTurn = ""
		self.players = []
		self.LastPlayerMove =""
		self.reservedSpots = []

class Player(object):
	def __init__(self, Ip, Port, Soc):
		self.playerIp = Ip
		self.playerPortNum = Port
		self.playerIcon = ""
		self.playerColor = ""
		self.playerSocket = Soc
