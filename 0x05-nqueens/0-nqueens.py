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

    def print_solution(board):
        solution = [[i, col] for i, col in enumerate(board)]
        print(solution)

    def solve(row):
        if row == N:
            print_solution(board)
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                solve(row + 1)
                board[row] = -1

    solve(0)


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
