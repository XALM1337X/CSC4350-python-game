
#Tic-Tac-Toe Game Interface

#Import Modules
from tkinter import *

class GameBoard:

    #Define Constructor 
    def __init__(self, token):

        #X or O for the player.
        self.gameToken = token

        
        self.gameWindow = Tk()

        self.canvas_width = 235
        self.canvas_height = 360

        self.canvas = Canvas(self.gameWindow, width=self.canvas_width, height=self.canvas_height)
        
        #First row of buttons
        self.b1 = Button(self.canvas, text = "", width=10, height=6, command=lambda: self.SetButtonToken(1))
        self.b1.place(x=0, y=0)

        self.b2 = Button(self.canvas, text ="", width=10, height=6, command=lambda: self.SetButtonToken(2))
        self.b2.place(x=80, y=0)

        self.b3 = Button(self.canvas, text ="", width=10, height=6, command=lambda: self.SetButtonToken(3))
        self.b3.place(x=160, y=0)

        #Second row of buttons
        self.b4 = Button(self.canvas, text ="", width=10, height=6, command=lambda: self.SetButtonToken(4))
        self.b4.place(x=0, y=100)

        self.b5 = Button(self.canvas, text ="", width=10, height=6, command=lambda: self.SetButtonToken(5))
        self.b5.place(x=80, y=100)

        self.b6 = Button(self.canvas, text ="", width=10, height=6, command=lambda: self.SetButtonToken(6))
        self.b6.place(x=160, y=100)

        #Third row of buttons
        self.b7 = Button(self.canvas, text ="", width=10, height=6, command=lambda: self.SetButtonToken(7))
        self.b7.place(x=0, y=200)
        
        self.b8 = Button(self.canvas, text ="", width=10, height=6, command=lambda: self.SetButtonToken(8))
        self.b8.place(x=80, y=200)

        self.b9 = Button(self.canvas, text ="", width=10, height=6, command=lambda: self.SetButtonToken(9))
        self.b9.place(x=160, y=200)

        
        self.canvas.pack()
      



        mainloop()

    #Function takes in a button ID and sets the corresponding X or O depending on gameToken.
    def SetButtonToken(self, button_id):

            #Depending on which button is selected, place the gameToken on that button and disable it so the user can no longer
            #place tokens there. 
            if button_id == 1:
                self.b1.config(text=self.gameToken, state=DISABLED)
            elif button_id == 2:
                self.b2.config(text=self.gameToken, state=DISABLED)
            elif button_id == 3:
                self.b3.config(text=self.gameToken, state=DISABLED)
            elif button_id == 4:
                self.b4.config(text=self.gameToken, state=DISABLED)
            elif button_id == 5:
                self.b5.config(text=self.gameToken, state=DISABLED)
            elif button_id == 6:
                self.b6.config(text=self.gameToken, state=DISABLED)
            elif button_id == 7:
                self.b7.config(text=self.gameToken, state=DISABLED)
            elif button_id == 8:
                self.b8.config(text=self.gameToken, state=DISABLED)
            elif button_id == 9:
                self.b9.config(text=self.gameToken, state=DISABLED)

        
def main():

    game_board = GameBoard("X")

