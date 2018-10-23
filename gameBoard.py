
#Tic-Tac-Toe Game Interface

#Import Modules
from tkinter import *

class GameBoard:

    #Define Constructor 
    def __init__(self, playerToken, playerColor, opponentToken, opponentColor):

        #X or O for the player (gameToken), color of player (playerColor), token of opponent, and color of opponent
        self.playerToken = playerToken
        self.playerColor = playerColor

        self.opponentToken = opponentToken
        self.opponentColor = opponentColor

        
        self.gameWindow = Tk()

        self.canvas_width = 320
        self.canvas_height = 500

        self.canvas = Canvas(self.gameWindow, width=self.canvas_width, height=self.canvas_height, bg="black")

        #Create Vertical Lines
        self.canvas.create_line(10,30,10,330, fill="red", width=5)
        self.canvas.create_line(110,30, 110, 330, fill="red", width=5)
        self.canvas.create_line(210,30,210,330, fill="red", width=5)
        self.canvas.create_line(310,30,310,330, fill="red", width=5)

        #Create Horizontal Lines
        self.canvas.create_line(10,30,310,30, fill="red", width=5)
        self.canvas.create_line(10,130,310,130, fill="red", width=5)
        self.canvas.create_line(10,230,310,230, fill="red", width=5)
        self.canvas.create_line(10,330,310,330, fill="red", width=5)

        #User in-game notifications text.
        self.userMessage = Label(self.canvas, text="",bg="black", fg=self.playerColor)
        self.userMessage.place(x=15,y=395)
        #Create QUIT button for the user to click.
        self.quitButton = Button(self.canvas, text="QUIT", width=15, height=2, bg='grey' , command=self.CloseWindow)
        self.quitButton.place(x=205,y=460)

        #Player Information Box
        self.canvas.create_rectangle(10,360,200,500, fill="black", outline="red", width=3)
        self.playerInformationText = Label(self.canvas, text="Player Information", bg="black", fg="red")
        self.playerInformationText.place(x=40,y=370)


        self.createWidgets()
        self.canvas.pack()

    #Can use this function later to create multiple pieces, quit buttons, etc...
    def createWidgets(self):
        self.titleText= self.canvas.create_text(160,15, text="TIC-TAC-TOE", font='Helevetica, 18 bold', fill="red")

        self.gameWindow.bind('<Button-1>', self.HandlePlayerSelection)

    #Sets ownership of a particular region, updates board
    def HandlePlayerSelection(self, event):
        x, y = event.x, event.y

        if (x >= 10 and x <=110) and (y >=30 and y <=130):
            self.canvas.create_text(60, 80, text=self.playerToken, fill=self.playerColor, font='Helevetica, 25 bold')
         
        elif (x >= 110 and x <=210) and (y >= 30 and y <= 130):
            self.canvas.create_text(160,80, text=self.playerToken, fill=self.playerColor, font='Helevetica, 25 bold')
            
        elif (x >= 210 and x <=310) and (y >= 30 and y <=130):
            self.canvas.create_text(260, 80, text=self.playerToken, fill=self.playerColor, font='Helevetica, 25 bold')

        elif (x >=10 and  x <=110) and (y >=130 and y <=230):
            self.canvas.create_text(60, 180, text=self.playerToken, fill=self.playerColor, font='Helevetica, 25 bold')

        elif (x >= 110 and x <=210) and (y >= 130 and y <= 230):
            self.canvas.create_text(160, 180, text=self.playerToken, fill=self.playerColor, font='Helevetica, 25 bold')

        elif (x >= 210 and x <=310) and (y >= 130 and y <= 230):
            self.canvas.create_text(260,180, text=self.playerToken, fill=self.playerColor, font='Helevetica, 25 bold')

        elif (x >= 10 and x <=110) and (y >=230 and y <= 330):
            self.canvas.create_text(60,280, text=self.playerToken, fill=self.playerColor, font='Helevetica, 25 bold')

        elif (x >=110 and x <=210) and (y >=230 and y <=330):
            self.canvas.create_text(160,280, text=self.playerToken, fill=self.playerColor, font='Helevetica, 25 bold')

        elif (x >= 210 and x <= 310) and (y >= 230 and y <=330):
            self.canvas.create_text(260,280, text=self.playerToken, fill=self.playerColor, font='Helevetica, 25 bold')
   

    def UpdateBoard(self, row, column):
        if row == 1 and column == 1:
            self.canvas.create_text(60, 80, text=self.opponentToken, fill=self.opponentColor, font='Helevetica, 25 bold')
            
        elif row == 1 and column == 2:
             self.canvas.create_text(160,80, text=self.opponentToken, fill=self.opponentColor, font='Helevetica, 25 bold')

        elif row == 1 and column == 3:
            self.canvas.create_text(260, 80, text=self.opponentToken, fill=self.opponentColor, font='Helevetica, 25 bold')

        elif row == 2 and column == 1:
            self.canvas.create_text(60, 180, text=self.opponentToken, fill=self.opponentColor, font='Helevetica, 25 bold')

        elif row == 2 and column == 2:
            self.canvas.create_text(160, 180, text=self.opponentToken, fill=self.opponentColor, font='Helevetica, 25 bold')

        elif row == 2 and column == 3:
            self.canvas.create_text(260,180, text=self.opponentToken, fill=self.opponentColor, font='Helevetica, 25 bold')

        elif row == 3 and column == 1:
            self.canvas.create_text(60,280, text=self.opponentToken, fill=self.opponentColor, font='Helevetica, 25 bold')

        elif row == 3 and column == 2:
            self.canvas.create_text(160,280, text=self.opponentToken, fill=self.opponentColor, font='Helevetica, 25 bold')

        elif row == 3 and column == 3:
            self.canvas.create_text(260,280, text=self.opponentToken, fill=self.opponentColor, font='Helevetica, 25 bold')


    #Function that sets the message notification to the player.
    def SetPlayerMessage(self, message):
        self.userMessage.config(text=message)
        

    #Function that clears the message notification. 
    def ClearPlayerMessage(self):
        self.userMessage.config(text="") 

    #Delete Window upon user clicking 'QUIT'.
    def CloseWindow(self):
        self.gameWindow.destroy()

    #Function to start the client application.
    def Start(self):
        self.gameWindow.mainloop()

            
        
def main():

    game_board = GameBoard("X", "blue", "O", "orange")


    #Unit testing for Set and Clearing of Messages
    game_board.SetPlayerMessage("Player Color: "+game_board.playerColor+"\nYour opponent's color is: "+game_board.opponentColor)
    game_board.ClearPlayerMessage()
    game_board.UpdateBoard(1,1)
    game_board.UpdateBoard(1,2)
    game_board.UpdateBoard(1,3)
    game_board.UpdateBoard(2,1)
    game_board.UpdateBoard(2,2)
    game_board.UpdateBoard(2,3)
    game_board.UpdateBoard(3,1)
    game_board.UpdateBoard(3,2)
    game_board.UpdateBoard(3,3)



    game_board.Start()
