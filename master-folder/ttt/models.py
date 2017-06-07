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

def check_for_win():
# check for rows are the same

    if board[0][0] == board[0][1] and board[0][0] == board[0][2]:
      print('win')
    elif board[1][0] == board[1][1] and board[1][0] == board[1][2]:
      print('win')
    elif board[2][0] == board[2][1] and board[2][0] == board[2][2]:
      print('win')
    else:
      print('no win')

def win_check_row():
    for r in board:
      if r[0] == r[1] == r[2] == "X":
        print('win')
      else:
        print('no win')

def win_check_column():
    for c in range(0, len(board[0])):
      if board[0][c] == board[1][c] == board[2][c] == "X":
        print('win')
      else:
        print('no win')

def win_check_diag():
    if board[0][0] == board[1][1] == board[2][2] == "X":
        print("win")
    elif board[0][2] == board[1][1] == board[2][0] == "X":
        print("win")
    else:
        print("no win")

def win_check():
    win_check_row()
    win_check_column()
    win_check_diag()

def receive_input(position):
    r, c = position
    board[r][c] = "X"


def main():
    while True:
        print_board(board)
        position = raw_input("Enter a position: ").split(" ")
        position = map(lambda a: int(a), position)
        receive_input(position)
        win_check()
        if raw_input("continue? y for yes") != "y":
            break


main()
