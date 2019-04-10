#Jaehlon Samuda and Thomas Armour
#Connect Four Project
#CSC2280


def show_board(board):

    #this function makes the board in text format with labels for the rows and columns
    print "   1   2   3   4    5   6   7"
    print "1: " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " | " + board[0][3] + " | " + board[0][4] + " | " + board[0][5] + " | " + board[0][6] + " | " + board[0][7]
    print "  ---+---+---+---+---+---+---"
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
print(show_board(connect4_board))

#circles is for the "circles" that you see when you play the game
#there are 42 circles in total so when there are no more circles left, the game should end
circles=42
while circles<=42:
    #asks user for input
    #player 1's move


    col = input("What col would you like to move to (1-7):")
    for row in range (6,0,-1):
        #this if statement checks if the number entered is valid and then puts their symbol in that column
        if (1 <= row <= 6) and (1 <= col <= 7) and (connect4_board[row-1][col-1] == " "):
            connect4_board[row-1][col-1] = 'O'
            circles=circles-1
            break

        if (checkwinner(connect4_board))== "O":
            print("Player O has won!")
        if (checkwinner(connect4_board) == 'X'):
            print("Player X has won!")

        print(checkwinner(connect4_board))

    #prints the board after every move
    print(show_board(connect4_board))

    #player 2's move
    col = input("What col would you like to move to (1-7):")
    for row in range (6,0,-1):
        if (1 <= row <= 6) and (1 <= col <= 7) and (connect4_board[row-1][col-1] == " "):
            connect4_board[row-1][col-1] = 'X'
            circles=circles-1
            break

        if (checkwinner(connect4_board) == 'X'):
            print("Player X has won!")
        if (checkwinner(connect4_board))== "O":
            print("Player O has won!")

        print(checkwinner(connect4_board))


    if circles==0:
        #if there are no more circles left on the board, it will break out of the loop
        break

    print(show_board(connect4_board))
    print(checkwinner(connect4_board))

print("Do you want to play again? ")
