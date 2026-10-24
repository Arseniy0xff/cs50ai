"""
Tic Tac Toe Player
"""

import math
from util import *

# from pygame.examples.setmodescale import flag

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xn, on = 0, 0
    for y in board:
        for x in y:
            if x == X:
                xn += 1
            elif x == O:
                on += 1
    return O if xn > on else X



def actions(board):
    pos_act = set()
    for i, y in enumerate(board):
        for j, x in enumerate(y):
            if x == EMPTY:
               pos_act.add((i, j))
    return pos_act


def result(board, action):
    new_board_state = [row.copy() for row in board]
    if new_board_state[action[0]][action[1]] is not EMPTY:
        raise Exception('are you fucker?')

    new_board_state[action[0]][action[1]] = player(new_board_state)

    return new_board_state


def winner(board):
    lines = []

    lines.extend(board)

    lines.extend([[board[row][col] for row in range(3)] for col in range(3)])

    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])

    for line in lines:
        if line[0] is not None and line[0] == line[1] == line[2]:
            return line[0]

    return None


def terminal(board):
    if winner(board) is not None:
        return True

    return all(cell is not None for row in board for cell in row)



def utility(board):
    r = winner(board)
    if r == X:
        return 1
    elif r == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    # if terminal(board):
    #     return None

    cact = ()

    def min_or_max(com_b, t):
        if t == X:
            return max(com_b, key=lambda i: i[0])
        elif t == O:
            return min(com_b, key=lambda i: i[0])

    def f(b):
        nonlocal cact
        if terminal(b):

            return utility(b)

        ab, ac = min_or_max([(f(result(b, a)), a) for a in list(actions(b))], player(b)) # here i can implemet optimazation
        cact = ac
        return ab


    f(board)
    return cact
