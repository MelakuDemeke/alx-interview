#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    """
    Check if it is safe to place a queen at a given position on the board.

    Args:
    - board: list of integers representing the current state of the board
    - row: integer representing the row to check
    - col: integer representing the column to check
    - N: integer representing the size of the board

    Returns:
    - True if it is safe to place a queen at the given position, False otherwise
    """
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N):
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N

    def print_solution(board):
        solution = [[i, col] for i, col in enumerate(board)]
        print(solution)