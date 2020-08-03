"""
Tic Tac Toe Player
"""

import copy
import math

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
    X_moves = sum([row.count(X) for row in board])
    O_moves = sum([row.count(O) for row in board])
    if X_moves > O_moves:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add((i,j))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    r,c = action
    if board[r][c] != EMPTY:
        raise Exception
    new = copy.deepcopy(board)
    new[r][c] = player(board)
    return new


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    def check_vertical(board):
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2]:
                return board[i][0]
        else:
            return None


    def check_horizontal(board):
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i]:
                return board[0][i]
        else:
            return None


    def check_diagon(board):
        if board[0][0] == board[1][1] == board[2][2]:
            return board[1][1]
        elif board[0][2] == board[1][1] == board[2][0]:
            return board[1][1]
        else:
            return None


    return check_vertical(board) or check_horizontal(board) or check_diagon(board)


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    EMPTY_cells = sum([row.count(EMPTY) for row in board])
    if winner(board):
        return True
    if EMPTY_cells:
        return False
    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if board[1][1] == EMPTY:
        return (1,1)

    max_deep = len(actions(board))

    def max_value(board):
        if terminal(board):
            return utility(board)
        v = -float('inf')
        for act in actions(board):
            v = max(v, min_value(result(board,act)))
        return v

    def min_value(board):
        if terminal(board):
            return utility(board)
        v = float('inf')
        for act in actions(board):
            v = min(v, max_value(result(board,act)))
        return v

    if player(board) == X:
        target = 'maximize'
        z = max_value(board)

    if player(board) == O:
        target = 'minimize'
        z = min_value(board)
