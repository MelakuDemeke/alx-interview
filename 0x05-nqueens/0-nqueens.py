#!/usr/bin/python3
'''N Queens Problem'''
import sys


def is_safe(board, row, col, N):
    for i in range(row):
        if (
            board[i] == col
            or board[i] - i == col - row
            or board[i] + i == col + row
        ):
            return False
    return True


def solve_nqueens(N):
    board = [-1] * N
    stack = []  # Use a stack to keep track of rows and columns

    def print_solution(board):
        solution = [[i, col] for i, col in enumerate(board)]
        print(solution)

    row = 0
    col = 0

    while row >= 0:
        if col < N:
            if is_safe(board, row, col, N):
                board[row] = col
                stack.append((row, col))
                row += 1
                col = 0
            else:
                col += 1
        else:
            if row == N:
                print_solution(board)
            if stack:
                row, col = stack.pop()
                board[row] = -1
                row += 1
                col += 1
            else:
                break


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)
