"""
Tic Tac Toe Player
"""

import math
import copy

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
    numX = 0
    numO = 0
    
    if terminal(board) is True:
        return X
    else: 
        for row in board:
            for space in row:
                if space == X:
                    numX = numX + 1
                elif space == O:
                    numO = numO + 1
        if numX > numO:
            return O
        elif numX == numO:
            return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board) is True:
        return (0,0)
    
    possibleMoves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possibleMoves.add((i,j))
    return possibleMoves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    """if action[0] != "2" or action[1] > 2: 
        raise IndexError
    if board[action[0]][action[1]] == X or board[action[0]][action[1]] == O:
        raise ValueError"""
        
    (i, j) = action
        
    if board[i][j] != EMPTY:
        print("Spot not available")
        raise IndexError
    
    copyBoard = copy.deepcopy(board)
    copyBoard[action[0]][action[1]] = player(board)
    return copyBoard 
    
        
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0]:
            return board[i][0]
        elif board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i]:
            return board[0][i]
    if board[0][0] == board[1][1] and board [1][1] == board [2][2] and board[0][0]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2]:
        return board[0][2]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    for i in range(3):
        for j in range(3):
            if not board[i][j]:
                return False
    count = 0
    for i in range(3): 
        for j in range(3):
            if board[i][j] == EMPTY: 
                count+=1
    if count == 9: 
        return False
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
    if terminal(board):
        return None
    
    """"numEmpty = 0
    for i in range(3): 
        for j in range(3): 
            if board[i][j] == EMPTY:
                numEmpty+=1
    if numEmpty == 9: 
        return (0,0)"""
    
    if player(board) == O:
        val = math.inf 
        move = set()
        for action in actions(board):
            k, count = maxValue(result(board, action), - math.inf, math.inf, 0)
            if k < val:
                val = k
                move = action
    elif player(board) == X:
        val = -math.inf
        move = set()
        for action in actions(board):
            k, count = minValue(result(board, action), -math.inf, math.inf, 0)
            if k > val:
                val = k
                move = action 
    return move
    
def maxValue(state, alpha, beta, count):
    if terminal(state):
        return utility(state), count + 1
    value = -math.inf
    for action in actions(state):
        val, count = minValue(result(state, action), alpha, beta, count)
        value = max(value, val)
        alpha = max(alpha, value)
        if alpha > beta: 
            break
    return value, count +1

def minValue(state, alpha, beta, count):
    if terminal(state):
        return utility(state), count +1
    value = math.inf
    for action in actions(state):
        val, count = maxValue(result(state, action), alpha, beta, count)
        value = min (value, val)
        beta = min(value, beta)
        if alpha > beta: 
            break 
    return value, count +1
