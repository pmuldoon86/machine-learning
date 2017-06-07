from django.db import models

# Create your models here.

board = []

for row in range(3): 
    board.append([])
    for column in range(3):
        board[row].append('.')

def print_board(board):
    for row in board:
        print(" ".join(row))

def input_marker(row, column, input_type):
    board[row][column] = input_type
    print_board(board)

def iterate_win_check_row():
    for r in board:
      if r[0] == r[1] == r[2]:
        return('win') 

def iterate_win_check_column():
    for c in range(0, len(board[0])):
      column = 0
      if board[0][c] == board[1][c] == board[2][c]:
        return('win') 

def win_check_diag():
      if board[0][0] == board[1][1] == board[2][2]:
        return('win')   
      elif board[0][2] == board[1][1] == board[2][0]:
        return('win') 
      else:
        return('no win')

def check_win()
    iterate_win_check_row
    iterate_win_check_column
    win_check_diag





print_board(board)



# board
# [
# [r1[0][1][2]]
# [r2[0][1][2]]
# [r3[0][1][2]]
# ]


