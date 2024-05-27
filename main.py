"""
Author: Aakaash Ghante
Program Name: FINAL PROJECT Tic-Tac-Toe!
Description: Make a tic-tac-toe game between two users and plot it
Date: 6/11/23
Version: 1.0
"""
# import modules
import ttt
import random
import matplotlib.pyplot as plt # type: ignore
# initalize variables/lists
replay = 1
playerTokens = ["X", "O"]
xWins = oWins = 0
draws = 0
# loop runs as long as user sets replay to 1
while replay == 1:
  # get game board and turn and tell users who goes first
  board = ttt.getGameBoard()
  turn = random.randint(0, 1)
  print ("{} goes first this round!".format(ttt.player(turn)))
  # loop will run until a draw or until it is broken
  for x in range (9):
    # print board and line and initialize valid
    ttt.printBoard(board)
    print ("")
    valid = False
    # valid will turn into true once a valid move is played ending the loop
    while valid == False:
      slot = int(input("{} choose a slot to play in: ".format(ttt.player(turn))))
      valid = ttt.validMove(board, slot)
      if valid:
        ttt.placeToken(board, slot, playerTokens[turn])
    if turn == 1:
      turn = 0
    else:
      turn = 1
    # check if someone won and if they did who won and add it to the win variable
    if ttt.checkWin(board):
      if ttt.detWinner(board) == "X":
        xWins += 1
      else:
        oWins += 1
        # break once someone wins
      break
  # add to the draws variable if the game is a draw
  if ttt.checkWin(board) == False:
    draws += 1
  # print final board and amount of wins and draws
  ttt.printBoard(board)
  print ("Player X Wins: {} | Player O Wins: {} | Draws: {}".format(xWins, oWins, draws))
  # ask user if they want to play again
  replay = int(input("Do you want to play again?\n1 = Yes\n2 = No\n"))
# games is the total amount of wins and draws
games = oWins + xWins + draws
# make the percentages from the games
percentages = [xWins/games*100, oWins/games*100, draws/games*100]
# if users played more than 1 game plot their wins and draws on a pie chart
if games > 1:
  winlabels = ["X Wins", "O Wins", "Draws"]
  plt.pie(percentages, labels = winlabels)
  plt.show()

