# function to make the gameboard
def getGameBoard():
  row1 = [1, 2, 3]
  row2 = [4, 5, 6]
  row3 = [7, 8, 9]
  gameBoard = [row1, row2, row3]
  return gameBoard
# function to print the game board (every turn)
def printBoard(board):
  for x in range (len(board)):
    gameRow = ""
    for y in range (len(board)):
      gameRow += str(board[x][y]) + " "
    print(gameRow)
# function to divide board into all rcds
def divideBoard(board):
  r1 = board[0]
  r2 = board[1]
  r3 = board[2]
  c1 = [r1[0], r2[0], r3[0]]
  c2 = [r1[1], r2[1], r3[1]]
  c3 = [r1[2], r2[2], r3[2]]
  d1 = [r1[0], r2[1], r3[2]]
  d2 = [r1[2], r2[1], r3[0]]
  divideBoard = [r1, r2, r3, c1, c2, c3, d1, d2]
  return divideBoard
# function used in detWinner and checkWin
def checkSame(rcd):
  previous = rcd[0]
  for l in range (len(rcd)):
    if previous != rcd[l]:
      return False
    previous = rcd[l]
  return True
# function to check who won
def detWinner(board):
  board = divideBoard(board)
  for x in range (len(board)):
    if checkSame(board[x]) == True:
      return board[x][0]
# function to check win
def checkWin(board):
  board = divideBoard(board)
  for x in range (len(board)):
    if checkSame(board[x]):
      return True
  return False
# function to check if X or O is already in the spot to see if user's move is valid or if it is even on the board
def validMove(board, slot):
  if 1 <= slot <= 9:
    for x in range (len(board)):
      if slot in board[x]:
        return True
    return False
# place users token where they chose (X or O)
def placeToken(board, slot, token):
  r1 = board[0]
  r2 = board[1]
  r3 = board[2]
  for x in range (3):
    if r1[x] == slot:
      r1[x] = token
    elif r2[x] == slot:
      r2[x] = token
    elif r3[x] == slot:
      r3[x] = token
# function to say who the player is based on the turn
def player(turn):
  if turn == 0:
    return "Player X"
  else:
    return "Player O"

