#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True