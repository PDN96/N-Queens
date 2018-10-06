#!/usr/bin/env python3
import sys

# Count # of pieces in given row
def count_on_row(board, row):
    sum =0
    for c in range(0,N):
        if board[row][c]==1:
            sum = sum + 1
    return sum

# Count # of pieces in given column
def count_on_col(board, col):
    sum = 0
    for r in range(0, N):
        if board[r][col] == 1:
            sum = sum + 1
    return sum

def count_pieces(board):
    sum =0
    for k in range(0,N):
        for l in range(0,N):
            if board[k][l] == 1:
                sum = sum+1
    return sum

def printable_board_k(board):
    new_board = [[0 for i in range(0,N)]for j in range(0,N)]
    for k in range(0,N):
        for l in range(0,N):
            if board[k][l] == 2:
                new_board[k][l] = "X"
            elif board[k][l] == 1:
                new_board[k][l] = "K"
            else:
                new_board[k][l] ="_"
    return new_board

def printable_board_q(board):
    new_board = [[0 for i in range(0,N)]for j in range(0,N)]
    for k in range(0,N):
        for l in range(0,N):
            if board[k][l] == 2:
                new_board[k][l] = "X"
            elif board[k][l] == 1:
                new_board[k][l] = "Q"
            else:
                new_board[k][l] ="_"
    return new_board

def printable_board_r(board):
    new_board = [[0 for i in range(0,N)]for j in range(0,N)]
    for k in range(0,N):
        for l in range(0,N):
            if board[k][l] == 2:
                new_board[k][l] = "X"
            elif board[k][l] == 1:
                new_board[k][l] = "R"
            else:
                new_board[k][l] ="_"
    return new_board

def print_board(board):
    for k in range(0,N):
        for l in range(0,N):
            if l < N:
                print(board[k][l], end = ' ')
            else:
                print(board[k][l], end = '')
        if k < N:
            print()


def add_piece(board, row, col):
    new_board = board[0:row] + [board[row][0:col] + [1,] + board[row][col+1:]] + board[row+1:]
    return new_board

def not_attacked_k(i,j, board):
    for k in range(0,N):
        for l in range(0,N):
            if (k+2 == i and l+1 == j) or (k-2 == i and l+1 == j) or(k+2 == i and l-1 == j) or (k-2 == i and l-1 == j) or (k+1 == i and l+2 == j) or (k-1 == i and l+2 == j) or(k+1 == i and l-2 == j) or (k-1 == i and l-2 == j):
                if board[k][l] == 1:
                    return False
    return True

def not_attacked_q(i, j, board):
    for k in range(0, N):
        if board[i][k] == 1 or board[k][j] == 1:
            return False
    for k in range(0, N):
        for l in range(0, N):
            if k + l == i + j or k - l == i - j:
                if board[k][l] == 1:
                    return False
    return True

def successors_k(board):
    succ = []
    for r in range(0,N):
        for c in range(0,N):
            if board[r][c]== 2:
                continue
            new_board = add_piece(board, r, c)
            if new_board != board and not_attacked_k(r,c,board):
                succ.append(new_board)
    return succ

def successors_q(board):
    empty_r = [i for i in range(0, N)]
#    empty_c = [i for i in range(0,N)]
    for r in range(0, N):
        for c in range(0, N):
            if board[r][c] == 1:
#                empty_c.remove(c)
                empty_r.remove(r)
    succ = []
    col = count_pieces(board)
    for r in empty_r:
        if board[r][col] == 2:
            continue
        new_board = add_piece(board, r, col)
        if new_board != board and not_attacked_q(r, col, board) and count_pieces(new_board) <= N:
            succ.append(new_board)
    return succ

def successors_r(board):
    empty_r = [i for i in range(0, N)]
#    empty_c = [i for i in range(0, N)]
    for r in range(0, N):
        for c in range(0, N):
            if board[r][c] == 1:
#                empty_c.remove(c)
                empty_r.remove(r)
    succ = []
    col = count_pieces(board)
    for r in empty_r:
        if board[r][col] == 2:
            continue
        new_board = add_piece(board, r, col)
        if new_board != board and count_pieces(new_board) <= N:
            succ.append(new_board)
    return succ

def is_goal_k(board):
    if count_pieces(board) == N:
        return True
    else:
        return False

def is_goal_q(board):
    return count_pieces(board) == N and \
        all([count_on_row(board, r) <= 1 for r in range(0, N)]) and \
        all([count_on_col(board, c) <= 1 for c in range(0, N)])

def solve_k(initial_board):
    fringe = [initial_board]
    while len(fringe) > 0:
        for s in successors_k( fringe.pop()):
            if is_goal_k(s):
                return(s)
            fringe.append(s)
    return False

def solve_q(initial_board):
    fringe = [initial_board]
    while len(fringe) > 0:
        for s in successors_q(fringe.pop()):
            if is_goal_q(s):
                return (s)
            fringe.append(s)
    return False

def solve_r(initial_board):
    fringe = [initial_board]
    while len(fringe) > 0:
        for s in successors_r(fringe.pop()):
            if is_goal_q(s):
                return (s)
            fringe.append(s)
    return False

arguments = sys.argv
type = arguments[1]
N = int(arguments[2])
number_of_blocked = int(arguments[3])
initial_board = [[0 for i in range(0, N)] for j in range(0, N)]

if number_of_blocked == 0:
    if type == "nknight":
        solution = solve_k(initial_board)
        if solution:
            print_board(printable_board_k(solution))
        else:
            print("No solution exists")

    elif type == "nqueen":
        solution = solve_q(initial_board)
        if solution:
            print_board(printable_board_q(solution))
        else:
            print("No solution exists")

    elif type == "nrook":
        solution = solve_r(initial_board)
        if solution:
            print_board(printable_board_r(solution))
        else:
            print("No solution exists")

else:
    blocked_x = [0 for i in range(0,number_of_blocked)]
    blocked_y = [0 for i in range(0,number_of_blocked)]

    for i in range(0, 2 * number_of_blocked, 2):
        count = int(i/2)
        blocked_x[count] = int(arguments[i + 4]) - 1
        blocked_y[count] = int(arguments[i + 5]) - 1
        #print(blocked_x[count],blocked_y[count])

    for i in range(0,number_of_blocked):
        initial_board[blocked_x[i]][blocked_y[i]] = 2

    if type == "nknight":
        solution = solve_k(initial_board)
        if solution:
            print_board(printable_board_k(solution))
        else:
            print("No solution exists")

    elif type == "nqueen":
        solution = solve_q(initial_board)
        if solution:
            print_board(printable_board_q(solution))
        else:
            print("No solution exists")

    elif type == "nrook":
        solution = solve_r(initial_board)
        if solution:
            print_board(printable_board_r(solution))
        else:
            print("No solution exists")

