#Jaehlon Samuda and Thomas Armour
#Connect Four Project
#CSC2280

import time
from graphics import *


def show_board(board):

    #this function makes the board in text format with labels for the rows and columns
    print "   1   2   3   4   5   6   7"
    print "1: " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " | " + board[0][3] + " | " + board[0][4] + " | " + board[0][5] + " | " + board[0][6] + " | " + board[0][7]
    print "  ---+---+---+---+---+---+---+"
    print "2: " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " | " + board[1][3] + " | " + board[1][4] + " | " + board[1][5] + " | " + board [1][6] + " | " + board [1][7]
    print "  ---+---+---+---+---+---+---+"
    print "3: " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " | " + board[2][3] + " | " + board [2][4] + " | " + board [2][5] + " | " + board [2][6] + " | " + board [2][7]
    print "  ---+---+---+---+---+---+---+"
    print "4: " + board[3][0] + " | " + board[3][1] + " | " + board[3][2] + " | " + board[3][3] + " | " + board [3][4] + " | " + board [3][5] + " | " + board [3][6] + " | " + board [3][7]
    print "  ---+---+---+---+---+---+---+"
    print "5: " + board[4][0] + " | " + board[4][1] + " | " + board[4][2] + " | " + board[4][3] + " | " + board [4][4] + " | " + board [4][5] + " | " + board [4][6] + " | " + board [4][7]
    print "  ---+---+---+---+---+---+---+"
    print "6: " + board[5][0] + " | " + board[5][1] + " | " + board[5][2] + " | " + board[5][3] + " | " + board [5][4] + " | " + board [5][5] + " | " + board [5][6] + " | " + board [5][7]
    print("")

def checkwinner(board):
    #this function checks for a winner
    #if there is no winner, the function will return  " "
    #if someone has won, it will return 'X' or "O" depending on the winner

    #checks the rows for a winner
    for row in range(6):
        for col in range(3):
            if (board[row][col] == board[row][col + 1] == board[row][col + 2] ==\
                board[row][col + 3]) and (board[row][col] != " "):
                return board[row][col]

    #checks the columns for a winner
    for col in range(6):
        for row in range(3):
            if (board[row][col] == board[row + 1][col] == board[row + 2][col] ==\
                board[row + 3][col]) and (board[row][col] != " "):
                return board[row][col]

    #checks the diagonals (top-left to bottom-right) for winner
    for row in range(3):
        for col in range(4):
            if (board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] ==\
                board[row + 3][col + 3]) and (board[row][col] != " "):
                return board[row][col]


    #checks the diagonals (bottom-left to top-right) for winner
    for row in range(5, 2, -1):
        for col in range(3):
            if (board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] ==\
                board[row - 3][col + 3]) and (board[row][col] != " "):
                return board[row][col]

    # No winner: return the empty string
    return ""

#this makes the initial graphics window with text
win= GraphWin(title= "CONNECT FOUR", width= 400, height= 400)
win.setBackground("blue")
txt=Text(Point(200,180), "CONNECT")
txt.setTextColor("red")
txt.setSize(30)
txt.setFace("courier")
txt.draw(win)
txt=Text(Point(200,220), "FOUR")
txt.setTextColor("yellow")
txt.setSize(30)
txt.setFace("courier")
txt.draw(win)

#makes the window stay open for 2 seconds before closing
time.sleep(2.00)
win.close()

#this is the main window where the game will be played
win = GraphWin(title="CONNECT FOUR", width= 400, height= 400)
win.setBackground(color_rgb(0,0,255))

#THESE ARE THE VERTICAL LINES
line1=Line(Point(57,0), Point(57,400))
line1.draw(win)

line2=Line(Point(114,0), Point(114,400))
line2.draw(win)

line3=Line(Point(171,0), Point(171,400))
line3.draw(win)

line4=Line(Point(228,0), Point(228,400))
line4.draw(win)

line5=Line(Point(285,0), Point(285,400))
line5.draw(win)

line6=Line(Point(342,0), Point(342,400))
line6.draw(win)

#THESE ARE THE HORIZONTAL LINES
row1=Line(Point(0,67), Point(400,67))
row1.draw(win)

row2=Line(Point(0,134), Point(400,134))
row2.draw(win)

row3=Line(Point(0,201), Point(400,201))
row3.draw(win)

row4=Line(Point(0,268), Point(400,268))
row4.draw(win)

row4=Line(Point(0,335), Point(400,335))
row4.draw(win)

#THESE ARE THE BLANK CIRCLES
#first column of gray circles
circ=Circle(Point(57*1-28,368),25)
circ.setFill(color_rgb(128,128,128))
circ.draw(win)

#loop to make the circles for each column
for i in range(6):
    circ=Circle(Point(57*1-28,368-i*66),25)
    circ.setFill(color_rgb(128,128,128))
    circ.draw(win)

#second column
circ=Circle(Point(57*2-28,368),25)
circ.setFill(color_rgb(128,128,128))
circ.draw(win)
for i in range(6):
    circ=Circle(Point(57*2-28,368-i*66),25)
    circ.setFill(color_rgb(128,128,128))
    circ.draw(win)

#third column
circ=Circle(Point(57*3-28,368),25)
circ.setFill(color_rgb(128,128,128))
circ.draw(win)
for i in range(6):
    circ=Circle(Point(57*3-28,368-i*66),25)
    circ.setFill(color_rgb(128,128,128))
    circ.draw(win)

#fourth columns
circ=Circle(Point(57*4-28,368),25)
circ.setFill(color_rgb(128,128,128))
circ.draw(win)
for i in range(6):
    circ=Circle(Point(57*4-28,368-i*66),25)
    circ.setFill(color_rgb(128,128,128))
    circ.draw(win)

#fifth column
circ=Circle(Point(57*5-28,368),25)
circ.setFill(color_rgb(128,128,128))
circ.draw(win)
for i in range(6):
    circ=Circle(Point(57*5-28,368-i*66),25)
    circ.setFill(color_rgb(128,128,128))
    circ.draw(win)

#sixth column
circ=Circle(Point(57*6-28,368),25)
circ.setFill(color_rgb(128,128,128))
circ.draw(win)
for i in range(6):
    circ=Circle(Point(57*6-28,368-i*66),25)
    circ.setFill(color_rgb(128,128,128))
    circ.draw(win)

#seventh row
circ=Circle(Point(57*7-28,368),25)
circ.setFill(color_rgb(128,128,128))
circ.draw(win)
for i in range(6):
    circ=Circle(Point(57*7-28,368-i*66),25)
    circ.setFill(color_rgb(128,128,128))
    circ.draw(win)

#this puts the positions of the boards in seperate lists
connect4_board = [ [ " ", " ", " ", " ", " ", " "," ", " "], [ " ", " ", " ", " ", " "," ", " ", " "], [ " ", " ", " ", " ", " ", " ", " ", " "], [ " ", " ", " ", " ", " ", " ", " ", " "], [ " ", " ", " ", " ", " ", " ", " ", " "], [ " ", " ", " ", " ", " ", " ", " ", " "] ]

#we wanted something big to grab the users' attention
print(" _______      ______                   ______")
print("|            |      |      |     |    |      |")
print("|-----       |      |      |     |    |______|")
print("|            |      |      |     |    |    \\")
print("|            |______|      |_____|    |     \\")
print("")

#a short introduction to our game
print("WELCOME TO OUR CONNECT FOUR GAME MADE OUT OF PYTHON CODE")
print("")

#prints an empty board to start the game with
show_board(connect4_board)

#circles is for the "circles" that you see when you play the game
#there are 42 circles in total so when there are no more circles left, the game should end
circles=42

#this list keeps track of the placement of "chips" on the board
placement= [0,0,0,0,0,0,0]

while circles<=42 and checkwinner(connect4_board)=="":

    #asks user for input
    #player 1's move
    col = input("What col would you like to move to (1-7):")
    for row in range (6,0,-1):

        #this if statement skips the player's turn if they enter an invalid column number
        if (col>7):
            print("That is an incorrect column. Your turn has been skipped.")
            rect=Rectangle(Point(86,130), Point(305,264))
            rect.setFill(color_rgb(128,128,128))
            rect.setOutline("black")
            rect.draw(win)
            txt1=Text(Point(200,200), "Invalid column." )
            txt1.setFace("helvetica")
            txt1.draw(win)
            txt2=Text(Point(200,220), "Your turn has been skipped.")
            txt2.setFace("helvetica")
            txt2.draw(win)
            time.sleep(1.50)
            txt1.undraw()
            txt2.undraw()
            rect.undraw()
            break

        #this if statement checks if the number column entered is valid and then puts their symbol in that column
        if (1 <= row <= 6) and (1 <= col <= 7) and (connect4_board[row-1][col-1] == " "):
            connect4_board[row-1][col-1] = 'O'
            circles=circles-1

            #makes the graphic for the circles
            circ=Circle(Point(57*col-28,368-placement[col-1]*66),25)
            circ.setFill("red")
            circ.draw(win)

            #this adjusts the list to update the placement of chips
            placement[col-1]+=1

            #checks if player O or Red has won the game
            if (checkwinner(connect4_board))== 'O':
                print("Player O has won!")

                #makes a rectangle for the text to go in
                rect=Rectangle(Point(86,130), Point(305,264))
                rect.setFill(color_rgb(128,128,128))
                rect.setOutline("black")
                rect.draw(win)

                #creates text that states that the player won the game
                txt=Text(Point(200,200), "Player Red has won!")
                txt.setFace("helvetica")
                txt.draw(win)
            break

        else:
            print("")

        #prints the winner if there is one
        print(checkwinner(connect4_board))

    #prints the board after every move
    show_board(connect4_board)
    print("Next player's move.")

    #player 2's move
    col = input("What col would you like to move to (1-7): ")
    for row in range (6,0,-1):
        if (col>7):
            print("That is an incorrect column. Please try again.")
            rect=Rectangle(Point(86,130), Point(305,264))
            rect.setFill(color_rgb(128,128,128))
            rect.setOutline("black")
            rect.draw(win)
            txt1=Text(Point(200,200), "Invalid column." )
            txt1.setFace("helvetica")
            txt1.draw(win)
            txt2=Text(Point(200,220), "Your turn has been skipped.")
            txt2.setFace("helvetica")
            txt2.draw(win)
            time.sleep(1.50)
            txt1.undraw()
            txt2.undraw()
            rect.undraw()
            break

        if (1 <= row <= 6) and (1 <= col <= 7) and (connect4_board[row-1][col-1] == " "):
            connect4_board[row-1][col-1] = 'X'
            circles=circles-1
            circ=Circle(Point(57*col-28,368-placement[col-1]*66),25)
            circ.setFill("yellow")
            circ.draw(win)
            placement[col-1]+=1

            #checks if yellow or X player has won
            if (checkwinner(connect4_board) =='X'):
                print("Player X has won!")
                rect=Rectangle(Point(86,130), Point(310,264))
                rect.setFill(color_rgb(128,128,128))
                rect.setOutline("black")
                rect.draw(win)
                txt=Text(Point(200,200), "The Yellow player has won!")
                txt.setFace("helvetica")
                txt.draw(win)
                break
            break


        if (checkwinner(connect4_board))== 'O':
            print("Player O has won!")
            rect=Rectangle(Point(86,130), Point(310,264))
            rect.setFill(color_rgb(128,128,128))
            rect.setOutline("black")
            rect.draw(win)
            txt=Text(Point(200,200), "The Red player has won!")
            txt.setFace("helvetica")
            txt.draw(win)
            break

        else:
            print("")

    #I had to put this here too because it wasn't properly checking inside of the loop
    if (checkwinner(connect4_board) =='X'):
                print("Player X has won!")
                rect=Rectangle(Point(86,130), Point(310,264))
                rect.setFill(color_rgb(128,128,128))
                rect.setOutline("black")
                rect.draw(win)
                txt=Text(Point(200,200), "The Yellow player has won!")
                txt.setFace("helvetica")
                txt.draw(win)
                break

    if circles==0:
        #if there are no more circles left on the board, it will break out of the loop
        print("This game has ended in a tie.")
        rect=Rectangle(Point(86,130), Point(310,264))
        rect.setFill(color_rgb(128,128,128))
        rect.setOutline("black")
        rect.draw(win)
        txt=Text(Point(200,200), "This game has ended in a tie.")
        txt.setFace("helvetica")
        txt.draw(win)
        break

    show_board(connect4_board)
    print(checkwinner(connect4_board))

#just thanks the user for playing
print("Thank you for playing!")
time.sleep(3.00)
win.close()
win= GraphWin(title= "CONNECT FOUR", width= 400, height= 400)
win.setBackground("blue")
txt=Text(Point(200,180), "Thank you ")
txt.setTextColor("red")
txt.setSize(30)
txt.setFace("courier")
txt.draw(win)
txt=Text(Point(200,220), "for playing!")
txt.setTextColor("yellow")
txt.setSize(30)
txt.setFace("courier")
txt.draw(win)

#waits for user to click the window to end the game
time.sleep(5.00)
win.close()
