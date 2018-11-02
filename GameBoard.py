

from tkinter import *

class GameBoard:

    #Define Constructor for GameBoard class.
    def __init__(self, token, color, opponentToken, opponentColor):

        self.gameWindow = Tk()
        #Initialize variables that our game will need about the client.
        self.playerToken = token
        self.playerColor = color
        self.playerTurn = True
        self.isWinner = False

        #Initialize variables that our game will need about the opposing client.
        self.opponentToken = opponentToken
        self.opponentColor = opponentColor

        #Initialize winning line color.
        self.winningLine = "yellow"

        #List for spots that are already taken in a game.
        self.ReservedSpots = []

        #Create a canvas with a set width and height.
        self.canvasWidth = 320
        self.canvasHeight = 500

        self.canvas = Canvas(self.gameWindow, width=self.canvasWidth, height=self.canvasHeight, bg="black")

        #Set our game title.
        self.titleText = self.canvas.create_text(160, 15, text="TIC-TAC-TOE", font="Helevectica, 18 bold", fill="red")

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

        #Create QUIT button for the user to click.
        self.quitButton = Button(self.canvas, text="QUIT", width=15, height=2, bg='grey' , command=self.CloseWindow)
        self.quitButton.place(x=205,y=460)

        #Player Information Box
        self.canvas.create_rectangle(10,360,200,500, fill="black", outline="red", width=3)
        self.playerInformationText = Label(self.canvas, text="Player Information", bg="black", fg="red")
        self.playerInformationText.place(x=40,y=370)

        #User in-game notifications text.
        self.userMessage = Label(self.canvas, text="",bg="black", fg=self.playerColor)
        self.userMessage.place(x=15,y=395)

        #Bind the left click of the mouse to the Handler function for a player selection.
        self.gameWindow.bind('<Button-1>', self.HandlePlayerSelection)

        #Pack everything to our canvas, so it can be rendered.
        self.canvas.pack()






    #Def IsReserved: Function to check and see if position on the gameboard is taken.
    def IsReserved(self, row, column):

        if (row, column) not in self.ReservedSpots:
            return False
        else:
            self.ReservedSpots.append((0,0))
            return True


    #Function that converts a click to a (row, column) tuple.
    def convertClickToRowColumn(self, x, y):

        row = 0
        column = 0

        if (x >= 10 and x <=110) and (y >=30 and y <=130) and not self.IsReserved(1,1):
            row = 1
            column = 1

        elif (x >= 110 and x <=210) and (y >= 30 and y <= 130) and not self.IsReserved(1,2):
            row = 1
            column = 2

        elif (x >= 210 and x <=310) and (y >= 30 and y <=130) and not self.IsReserved(1,3):
            row = 1
            column = 3

        elif (x >=10 and  x <=110) and (y >=130 and y <=230) and not self.IsReserved(2,1):
            row = 2
            column = 1

        elif (x >= 110 and x <=210) and (y >= 130 and y <= 230) and not self.IsReserved(2,2):
            row = 2
            column = 2

        elif (x >= 210 and x <=310) and (y >= 130 and y <= 230) and not self.IsReserved(2,3):
            row = 2
            column = 3

        elif (x >= 10 and x <=110) and (y >=230 and y <= 330) and not self.IsReserved(3,1):
            row = 3
            column = 1

        elif (x >=110 and x <=210) and (y >=230 and y <=330) and not self.IsReserved(3,2):
            row = 3
            column = 2

        elif (x >= 210 and x <= 310) and (y >= 230 and y <=330) and not self.IsReserved(3,3):
            row = 3
            column = 3

        return (row, column)

    #Def HandlePlayerSelection: Function that places the player's corresponding X or O in the
    #Corresponding clicked area.
    def HandlePlayerSelection(self, event):

        #Get x and y coordinates of the mouse.
        x, y = event.x, event.y

        #Get (row, column) tuple from click.
        row_column = self.convertClickToRowColumn(x, y)
        row = row_column[0]
        column = row_column[1]

        #Clear out the message if there is one.
        self.ClearPlayerMessage()

        if self.playerTurn:

            if self.IsReserved(row, column):
                self.ClearPlayerMessage()
                self.SetPlayerMessage("SPOT ALREADY TAKEN!\nSELECT AGAIN!")

            else:

                if row == 1 and column == 1 and not self.IsReserved(row, column):
                    self.canvas.create_text(60, 80, text=self.playerToken, fill=self.playerColor, font='Helevetica, 25 bold')
                    self.ReservedSpots.append(row_column)

                elif row == 1 and column == 2 and not self.IsReserved(row, column):
                    self.canvas.create_text(160,80, text=self.playerToken, fill=self.playerColor, font='Helevetica, 25 bold')
                    self.ReservedSpots.append(row_column)

                elif row == 1 and column == 3 and not self.IsReserved(row, column):
                    self.canvas.create_text(260, 80, text=self.playerToken, fill=self.playerColor, font='Helevetica, 25 bold')
                    self.ReservedSpots.append(row_column)

                elif row == 2 and column == 1 and not self.IsReserved(row, column):
                    self.canvas.create_text(60, 180, text=self.playerToken, fill=self.playerColor, font='Helevetica, 25 bold')
                    self.ReservedSpots.append(row_column)

                elif row == 2 and column == 2 and not self.IsReserved(row, column):
                    self.canvas.create_text(160, 180, text=self.playerToken, fill=self.playerColor, font='Helevetica, 25 bold')
                    self.ReservedSpots.append(row_column)

                elif row == 2 and column == 3 and not self.IsReserved(row, column):
                    self.canvas.create_text(260,180, text=self.playerToken, fill=self.playerColor, font='Helevetica, 25 bold')
                    self.ReservedSpots.append(row_column)

                elif row == 3 and column == 1 and not self.IsReserved(row, column):
                    self.canvas.create_text(60,280, text=self.playerToken, fill=self.playerColor, font='Helevetica, 25 bold')
                    self.ReservedSpots.append(row_column)

                elif row == 3 and column == 2 and not self.IsReserved(row, column):
                    self.canvas.create_text(160,280, text=self.playerToken, fill=self.playerColor, font='Helevetica, 25 bold')
                    self.ReservedSpots.append(row_column)

                elif row == 3 and column == 3 and not self.IsReserved(row, column):
                    self.canvas.create_text(260,280, text=self.playerToken, fill=self.playerColor, font='Helevetica, 25 bold')
                    self.ReservedSpots.append(row_column)




    #Def UpdateBoard: Function places opponent token on game board. Takes in a row and column

    def UpdateBoard(self, row, column):
        if row == 1 and column == 1:
            self.canvas.create_text(60, 80, text=self.opponentToken, fill=self.opponentColor, font='Helevetica, 25 bold')
            self.ReservedSpots.append((1,1))


        elif row == 1 and column == 2:
             self.canvas.create_text(160,80, text=self.opponentToken, fill=self.opponentColor, font='Helevetica, 25 bold')
             self.ReservedSpots.append((1,2))

        elif row == 1 and column == 3:
            self.canvas.create_text(260, 80, text=self.opponentToken, fill=self.opponentColor, font='Helevetica, 25 bold')
            self.ReservedSpots.append((1,3))
			
        elif row == 2 and column == 1:
            self.canvas.create_text(60, 180, text=self.opponentToken, fill=self.opponentColor, font='Helevetica, 25 bold')
            self.ReservedSpots.append((2,1))
			
        elif row == 2 and column == 2:
            self.canvas.create_text(160, 180, text=self.opponentToken, fill=self.opponentColor, font='Helevetica, 25 bold')
            self.ReservedSpots.append((2,2))
			
        elif row == 2 and column == 3:
            self.canvas.create_text(260,180, text=self.opponentToken, fill=self.opponentColor, font='Helevetica, 25 bold')
            self.ReservedSpots.append((2,3))
			
        elif row == 3 and column == 1:
            self.canvas.create_text(60,280, text=self.opponentToken, fill=self.opponentColor, font='Helevetica, 25 bold')
            self.ReservedSpots.append((3,1))
			
        elif row == 3 and column == 2:
            self.canvas.create_text(160,280, text=self.opponentToken, fill=self.opponentColor, font='Helevetica, 25 bold')
            self.ReservedSpots.append((3,2))
			
        elif row == 3 and column == 3:
            self.canvas.create_text(260,280, text=self.opponentToken, fill=self.opponentColor, font='Helevetica, 25 bold')
            self.ReservedSpots.append((3,3))

    #Def DrawWinner: Function that draws winning line when a winner is declared.
    def DrawWinner(self, message):

        if message == "row_one":
            self.canvas.create_line(15,75,300,75, fill=self.winningLine, width=3)

        elif message == "row_two":
            self.canvas.create_line(15,175,300,175, fill=self.winningLine, width=3)

        elif message == "row_three":
            self.canvas.create_line(15,275,300,275, fill=self.winningLine, width=3)

        elif message == "column_one":
            self.canvas.create_line(60, 40, 60, 310, fill=self.winningLine, width=3)

        elif message == "column_two":
            self.canvas.create_line(160, 40, 160, 310, fill=self.winningLine, width=3)

        elif message == "column_three":
            self.canvas.create_line(260, 40, 260, 310, fill=self.winningLine, width=3)

        elif message == "diagonal_left":
            self.canvas.create_line(15,34,300,320, fill=self.winningLine, width=3)

        elif message == "diagonal_right":
            self.canvas.create_line(15,320,300,34, fill=self.winningLine, width=3)


    #Delete Window upon user clicking 'QUIT'.
    def CloseWindow(self):
        self.gameWindow.destroy()


    #Def SetPlayerMessage: Function takes in a string and displays the corresponding message
    #in the user interface.
    def SetPlayerMessage(self, message):
        self.userMessage.config(text=message)

    #Def ClearPlayerMessage: Function clears any message notification text.
    def ClearPlayerMessage(self):
        self.userMessage.config(text="")


    def Start(self):
        self.gameWindow.mainloop()
