# Author: Carter Fang
# Purpose: Tic Tac Toe game with an AI

# Initialize global board state, 3x3 grid -----
global board
board = [['','',''],
         ['','',''],
         ['','','']]


# Functions for checking win-conditions ------
def diagWin(char):
    if board[0][0]==char and board[1][1]==char and board[2][2]==char:
        return True
    elif board[0][2]==char and board[1][1]==char and board[2][0]==char:
        return True
    else:
        return False

def colWin(char):
    if board[0][0]==char and board[1][0]==char and board[2][0]==char:
        return True
    elif board[0][1]==char and board[1][1]==char and board[2][1]==char:
        return True
    elif board[0][2]==char and board[1][2]==char and board[2][2]==char:
        return True
    else:
        return False

def rowWin(char):
    if board[0][0] == char and board[0][1] == char and board[0][2] == char:
        return True
    elif board[1][0] == char and board[1][1] == char and board[1][2] == char:
        return True
    elif board[2][0] == char and board[2][1] == char and board[2][2] == char:
        return True
    else:
        return False

def checkWinner():
    if diagWin('O') or diagWin('X'):
        if(diagWin('O')):
            return 'O'
        else:
            return 'X'
    elif rowWin('O') or rowWin('X'):
        if(rowWin('O')):
            return 'O'
        else:
            return 'X'
    elif colWin('O') or colWin('O'):
        if(colWin('O')):
            return 'O'
        else:
            return 'X'
    else:
        return 'N'

# Purpose: Check validity of a requested move
# Output: True if valid, else false
def isOccupied(board, row, col):
    if board[row][col] == '':
        return False
    else:
        return True

# Purpose: Render the board in console using print()
def renderBoard(board):
    for row in range(3):
        print(board[row])

# Purpose: Find row and col indices of unoccupied spaces
# Output: List of 2x1 elements, each is an unoccupied space
def findEmpty(board):
    moves = []
    for row in range(3):
        for col in range(3):
            if not isOccupied(board, row, col):
                moves.append([row,col])

    return moves

# Assumption: PC is 'O'
# Purpose: Determine optimal move for computer player using minmax algorithm
# Output: Optimal move as a 2x1 element [row, col]
def optimalMove(pcChar):
    availMoves = findEmpty(board)
    scores = []

    for move in availMoves:
        board[move[0]][move[1]] = pcChar
        scores.append(minmax('X',0))
        board[move[0]][move[1]] = ''

    if availMoves == []:
        return None
    else:
        return availMoves[scores.index(max(scores))]


# Purpose: Helper function for optimal Move. Evaluates probability of winning
#          for each valid move on the board.
#          Given a current board state, computer character 'playerB', human character 'playerA'
#          Find and evaluate the terminal states for all possible moves
# Output: Return score of the current state
def minmax(currChar, score):

    availMoves = findEmpty(board)

    if checkWinner() == 'N' and len(availMoves) != 0:

        #For each available slot, place currChar there
        #Run minmaxHelp
        #Remove currChar from there
        for move in availMoves:
            board[move[0]][move[1]] = currChar
            if currChar == 'X':
                #print('Placed an X')
                score = score + minmax('O', score)
            elif currChar == 'O':
                #print('Placed an O')
                score = score + minmax('X', score)
            board[move[0]][move[1]] = ''

            return score

    elif checkWinner() == 'X':
        # Scale score by number of moves taken
        return score-(10/(9-len(availMoves)))

    elif checkWinner() == 'O':
        return score+(10/(9-len(availMoves)))

    else:
        return score


# THE GAME -------------------
def tictactoe():
    playerA = 'X'
    playerB = 'O'
    aiEnabled = True
    renderBoard(board)
    
    # Check for a winner ---
    while(checkWinner() == 'N'):
        
        # Take inputs ---
        # Player A turn
        while(1):
            print('PLAYER A TURN\n')
            row = input('Enter row:')
            row = ord(row) % 48;
            col = input('\nEnter col:')
            col = ord(col) % 48;
            
            # Evaluate move validity ---
            if isOccupied(board, row, col):
                print('Invalid space. Try again.\n')
            else:
                break

        board[row][col] = playerA

        # Computer/Player B turn
        if aiEnabled == True:
            aiMove = optimalMove(playerB) 

            if aiMove == None:
                print('It\'s a tie!')
                return

        else:
            while(1):
                print('PLAYER B TURN\n')
                row = input('Enter row:')
                row = ord(row) % 48;
                col = input('\nEnter col:')
                col = ord(col) % 48;
                
                # Evaluate move validity ---
                if isOccupied(board, row, col):
                    print('Invalid space. Try again.\n')
                else:
                    break

        
        board[aiMove[0]][aiMove[1]] = playerB
        renderBoard(board)
        
    # Outside game loop, winner has been found ---
    winner = checkWinner()
    print('Congratulations player ' + winner + '!')

tictactoe()