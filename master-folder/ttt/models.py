# from django.db import models
#
# # Create your models here.
#
# board = []
#
# for row in range(3):
#     board.append([])
#     for column in range(3):
#         board[row].append('.')
#
# def print_board(board):
#     for row in board:
#         print(" ".join(row))
#
# def input_marker(row, column, input_type):
#     board[row][column] = input_type
#     print_board(board)
#
# def check_for_win():
# # check for rows are the same
#
#     if board[0][0] == board[0][1] and board[0][0] == board[0][2]:
#       print('win')
#     elif board[1][0] == board[1][1] and board[1][0] == board[1][2]:
#       print('win')
#     elif board[2][0] == board[2][1] and board[2][0] == board[2][2]:
#       print('win')
#     else:
#       print('no win')
#
# def iterate_win_check_row():
#     for r in board:
#       if r[0] == r[1] == r[2]:
#         print('win')
#       else:
#         print('no win')
#
# def iterate_win_check_column():
#     for c in board:
#       if [0]c == [1]c == [2]c:
#         print('win')
#       else:
#         print('no win')
#
#
# print_board(board)
