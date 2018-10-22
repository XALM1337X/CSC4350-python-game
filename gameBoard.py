
#Tic-Tac-Toe Game Interface

#Import Modules
from tkinter import *

class GameBoard:

    #Define Constructor 
    def __init__(self, token, playerColor):

        #X or O for the player.
        self.gameToken = token
        self.playerColor = playerColor

        
        self.gameWindow = Tk()

        self.canvas_width = 235
        self.canvas_height = 360

        self.canvas = Canvas(self.gameWindow, width=self.canvas_width, height=self.canvas_height, bg="black")

        #User in-game notifications text.
        self.userMessage = Label(self.canvas, text="", bg="black", fg="white")
        self.userMessage.place(x=self.canvas_width/10, y=320)
        
        #First row of buttons
        self.b1 = Button(self.canvas, text = "", width=10, height=6, bg='grey', command=lambda: self.SetButtonOwnership(1))
        self.b1.place(x=0, y=0)

        self.b2 = Button(self.canvas, text ="", width=10, height=6, bg='grey', command=lambda: self.SetButtonOwnership(2))
        self.b2.place(x=80, y=0)

        self.b3 = Button(self.canvas, text ="", width=10, height=6, bg='grey', command=lambda: self.SetButtonOwnership(3))
        self.b3.place(x=160, y=0)

        #Second row of buttons
        self.b4 = Button(self.canvas, text ="", width=10, height=6, bg='grey', command=lambda: self.SetButtonOwnership(4))
        self.b4.place(x=0, y=100)

        self.b5 = Button(self.canvas, text ="", width=10, height=6, bg='grey',command=lambda: self.SetButtonOwnership(5))
        self.b5.place(x=80, y=100)

        self.b6 = Button(self.canvas, text ="", width=10, height=6, bg='grey', command=lambda: self.SetButtonOwnership(6))
        self.b6.place(x=160, y=100)

        #Third row of buttons
        self.b7 = Button(self.canvas, text ="", width=10, height=6, bg='grey', command=lambda: self.SetButtonOwnership(7))
        self.b7.place(x=0, y=200)
        
        self.b8 = Button(self.canvas, text ="", width=10, height=6, bg='grey', command=lambda: self.SetButtonOwnership(8))
        self.b8.place(x=80, y=200)

        self.b9 = Button(self.canvas, text ="", width=10, height=6,bg='grey', command=lambda: self.SetButtonOwnership(9))
        self.b9.place(x=160, y=200)

        self.quitButton = Button(self.canvas, text="QUIT", width=9, height=2, bg='grey' , command=self.CloseWindow)
        self.quitButton.place(x=165,y=320)


        self.canvas.pack()
      



        

    #Function takes in a button ID and sets the corresponding X or O depending on gameToken.
    def SetButtonOwnership(self, button_id):

            #Depending on which button is selected, place the gameToken on that button and disable it so the user can no longer
            #place tokens there. 
            if button_id == 1:
                self.b1.config(text=self.gameToken, bg=self.playerColor)
            elif button_id == 2:
                self.b2.config(text=self.gameToken, bg=self.playerColor)
            elif button_id == 3:
                self.b3.config(text=self.gameToken, bg=self.playerColor)
            elif button_id == 4:
                self.b4.config(text=self.gameToken, bg=self.playerColor)
            elif button_id == 5:
                self.b5.config(text=self.gameToken, bg=self.playerColor)
            elif button_id == 6:
                self.b6.config(text=self.gameToken, bg=self.playerColor)
            elif button_id == 7:
                self.b7.config(text=self.gameToken, bg=self.playerColor)
            elif button_id == 8:
                self.b8.config(text=self.gameToken, bg=self.playerColor)
            elif button_id == 9:
                self.b9.config(text=self.gameToken, bg=self.playerColor)


    #Function that sets the message notification to the player.
    def SetPlayerMessage(self, message):
        self.userMessage.config(text=message)

    #Function that clears the message notification. 
    def ClearPlayerMessage(self):
        self.userMessage.config(text="") 

    #Delete Window upon user clicking 'QUIT'.
    def CloseWindow(self):
        self.gameWindow.destroy()

    def CreateWinnerStrike(self, typeOfWin):
        if typeOfWin == "one_up_down":
            self.canvas.create_line(40,10,40,360,width=2, fill='red')
            #self.canvas.pack(side=TOP)
            
        
def main():

    game_board = GameBoard("X", "blue")


    #Unit testing for Set and Clearing of Messages
    game_board.SetPlayerMessage("PLAYER TWO WINS!\nPlease select quit")
    #game_board.ClearPlayerMessage()
    game_board.CreateWinnerStrike("one_up_down")

    game_board.gameWindow.mainloop()
