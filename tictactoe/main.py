
global board
board = [['','',''],
         ['','',''],
         ['','','']]

def playerMove():
    text = input("prompt")
    return text

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

def isOccupied(board, row, col):
    if board[row][col] == '':
        return False
    else:
        return True

def renderBoard(board):
    for row in range(3):
        print(board[row])

# Return row and col indices of unoccupied spaces
def findEmpty(board):
    moves = []
    for row in range(3):
        for col in range(3):
            if not isOccupied(board, row, col):
                moves.append([row,col])

    return moves

# Assumes PC is 'O' at the moment
def optimalMove(pcChar):
    availMoves = findEmpty(board)
    #print('Available moves are')
    #print(availMoves)
    scores = []

    for move in availMoves:
        board[move[0]][move[1]] = pcChar
        scores.append(minmax('X',0))
        board[move[0]][move[1]] = ''

    #print(scores)
    return availMoves[scores.index(max(scores))]



# Given a current board state, computer character 'playerB', human character 'playerA'
# Evaluate the terminal states for all possible moves
# Return the move with the highest total scores
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
        #print('Loss')
        #renderBoard(board)
        #print('\n')
        return score-(10/(9-len(availMoves)))

    elif checkWinner() == 'O':
        #print('Win')
        #renderBoard(board)
        #print('\n')
        return score+(10/(9-len(availMoves)))

    else:
        return score


def tictactoe():
    playerA = 'X'
    playerB = 'O'
    aiEnabled = True
    renderBoard(board)

    while(checkWinner() == 'N'):
        # Player A turn
        while(1):
            print('PLAYER A TURN\n')
            row = input('Enter row:')
            row = ord(row) % 48;
            col = input('\nEnter col:')
            col = ord(col) % 48;

            if isOccupied(board, row, col):
                print('Invalid space. Try again.\n')
            else:
                break

        board[row][col] = playerA

        # Computer/Player B turn
        if aiEnabled == True:
            [row, col] = optimalMove(playerB)
        else:
            while(1):
                print('PLAYER B TURN\n')
                row = input('Enter row:')
                row = ord(row) % 48;
                col = input('\nEnter col:')
                col = ord(col) % 48;

                if isOccupied(board, row, col):
                    print('Invalid space. Try again.\n')
                else:
                    break

        board[row][col] = playerB
        renderBoard(board)

    winner = checkWinner()
    print('Congratulations player ' + winner + '!')

tictactoe()