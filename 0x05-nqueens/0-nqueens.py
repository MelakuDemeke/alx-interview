#!/usr/bin/python3
'''N Queens Challenge'''

import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        board_size = int(sys.argv[1])  # 'n' renamed to 'board_size'
    except ValueError:
        print('N must be a number')
        exit(1)

    if board_size < 4:
        print('N must be at least 4')
        exit(1)

    solutions = []
    queens_on_board = []  # Renamed 'placed_queens' to 'queens_on_board'
    stop_search = False
    current_row = 0
    current_col = 0

    # Iterate through rows
    while current_row < board_size:
        need_to_go_back = False
        # Iterate through columns
        while current_col < board_size:
            # Check if the current column is safe
            is_safe = True
            for coord in queens_on_board:
                col = coord[1]
                if (
                    col == current_col or
                    col + (current_row - coord[0]) == current_col or
                        col - (current_row - coord[0]) == current_col):
                    is_safe = False
                    break

            if not is_safe:
                if current_col == board_size - 1:
                    need_to_go_back = True
                    break
                current_col += 1
                continue

            # Place the queen
            queen_coordinates = [current_row, current_col]
            queens_on_board.append(queen_coordinates)

            if current_row == board_size - 1:
                solutions.append(queens_on_board[:])
                for coord in queens_on_board:
                    if coord[1] < board_size - 1:
                        current_row = coord[0]
                        current_col = coord[1]
                for i in range(board_size - current_row):
                    queens_on_board.pop()

                if (current_row == board_size - 1 and
                        current_col == board_size - 1):
                    queens_on_board = []
                    stop_search = True

                current_row -= 1
                current_col += 1
            else:
                current_col = 0
            break

        if stop_search:
            break

        # On failure: go back to the previous row
        # and continue from the last safe column + 1
        if need_to_go_back:
            current_row -= 1
            while current_row >= 0:
                current_col = queens_on_board[current_row][1] + 1
                del queens_on_board[current_row]
                if current_col < board_size:
                    break
                current_row -= 1
            if current_row < 0:
                break
            continue
        current_row += 1

    for idx, solution in enumerate(solutions):
        if idx == len(solutions) - 1:
            print(solution, end='')
        else:
            print(solution)
