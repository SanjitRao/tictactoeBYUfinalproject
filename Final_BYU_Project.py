import random
class TicTacToe():
    def __init__(self,board):
        self.board=board
    def drawBoard(self):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
        print('   |   |')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('   |   |')

    def inputPlayerLetter(self):
        # Lets the player type which letter they want to be.
        # Returns a list with the player's letter as the first item, and the computer's letter as the second.
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Player 1: Do you want to be X or O?')
            letter = input().upper()

        # the first element in the tuple is the player's letter, the second is the computer's letter.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def whoGoesFirst(self):
        # Randomly choose the player who goes first.
        if random.randint(0, 1) == 0:
            return 'PLAYER 1'
        else:
            return 'PLAYER 2'
    def playAgain(self):
        # This function returns True if the player wants to play again, otherwise it returns False.
        willPlayAgain = input('Do you want to play again? (yes or no)').lower()
        if 'yes' in willPlayAgain:
            return True
        else:
            return False

    def makeMove(self, letter, move):
        self.board[move] = letter

    def isWinner(self,bo, le):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
        (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
        (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
        (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
        (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
        (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
        (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
        (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

    def getBoardCopy(self):
        # Make a duplicate of the board list and return it the duplicate.
        dupeBoard = []

        for i in self.board:
            dupeBoard.append(i)

        return dupeBoard

    def isSpaceFree(self, move):
        # Return true if the passed move is free on the passed board.
        return self.board[move] == ' '#If board[6] == ''. then isSpaceFree returns True

    def getPlayerMove(self):
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.isSpaceFree(int(move)):
            print('What is your next move? (1-9)')#say I chose 6, then 'move not in '123456789' is FALSE, and isSpaceFree returns FALSE, meaning the entire expression is false, therefore it jumps out of the while loop
            move = input()
        return int(move)

    def chooseRandomMoveFromList(self, movesList):
        # Returns a valid move from the passed list on the passed board.
        # Returns None if there is no valid move.
        possibleMoves = []
        for i in movesList:
            if self.isSpaceFree(self, i):
                possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

    def getComputerMove(self, computerLetter):
        # Given a board and the computer's letter, determine where to move and return that move.
        if computerLetter == 'X':
            playerLetter = 'O'
        else:
            playerLetter = 'X'

        # Here is our algorithm for our Tic Tac Toe AI:
        # First, check if we can win in the next move
        for i in range(1, 10):
            copy = getBoardCopy(self.board)
            if self.isSpaceFree(copy, i):
                makeMove(copy, computerLetter, i)
                if isWinner(copy, computerLetter):
                    return i

        # Check if the player could win on his next move, and block them.
        for i in range(1, 10):
            copy = getBoardCopy(board)
            if self.isSpaceFree(copy, i):
                makeMove(copy, playerLetter, i)
                if isWinner(copy, playerLetter):
                    return i

        # Try to take one of the corners, if they are free.
        move = chooseRandomMoveFromList(self, [1, 3, 7, 9])
        if move != None:
            return move

        # Try to take the center, if it is free.
        if self.isSpaceFree(self.board, 5):
            return 5

        # Move on one of the sides.
        return chooseRandomMoveFromList(self, [2, 4, 6, 8])

    def isBoardFull(self):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.isSpaceFree(i):
                return False
        return True


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    ttobj = TicTacToe(theBoard)
    playerLetter,computerLetter= ttobj.inputPlayerLetter()
    turn = ttobj.whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'PLAYER 1':
            #Player's turn.
            #drawBoard(theBoard)
            move = ttobj.getPlayerMove()
            ttobj.makeMove(playerLetter, move)
            print()
            if ttobj.isWinner(theBoard,playerLetter):
                ttobj.drawBoard()
                print('Hooray! ' + turn +' has won the game!')
                gameIsPlaying = False
            else:
                if ttobj.isBoardFull():
                    ttobj.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    ttobj.drawBoard()
                    turn = 'PLAYER 2'
                    print('Now it is '+turn+'\'s turn to move')

        else:
            # Computer's turn.
            #move = getComputerMove(theBoard, computerLetter)
            move = ttobj.getPlayerMove()
            ttobj.makeMove(computerLetter, move)
            print()
            if ttobj.isWinner(theBoard, computerLetter):
                ttobj.drawBoard()
                print('Hooray! ' + turn +' has won the game!')
                gameIsPlaying = False
            else:
                if ttobj.isBoardFull():
                    ttobj.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    ttobj.drawBoard()
                    turn = 'PLAYER 1'
                    print('Now it is ' + turn + '\'s turn to move')

    if not ttobj.playAgain():
        break
