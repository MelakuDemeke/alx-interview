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
    pass