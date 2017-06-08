from django.db import models

# Create your models here.

board = []

def create_board():
    global board
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

def win_check_row(letter):
    for r in board:
      if r[0] == r[1] == r[2] == letter:
        return('win')


def win_check_column(letter):
    for c in range(0, len(board[0])):
      if board[0][c] == board[1][c] == board[2][c] == letter:
        return('win')


def win_check_diag(letter):
    if board[0][0] == board[1][1] == board[2][2] == letter:
        return("win")
    elif board[0][2] == board[1][1] == board[2][0] == letter:
        return("win")
    else:
        return False

def win_check(letter):
    if win_check_row(letter) == "win" or win_check_column(letter) == "win" or win_check_diag(letter) =="win":
        return "win"

def receive_input(position, letter):
    r, c = position
    board[r][c] = letter


def main():
    create_board()
    print_board(board)
    while True:

        position = raw_input("Enter a position: ").split(" ")
        position = map(lambda a: int(a), position)
        receive_input(position, "X")
        print_board(board)
        if win_check("X") == "win":
            print "You've won!!!"
            if raw_input("Play again? Enter y for yes: ") == "y":
                main()
            else:
                break


main()
