import helpers
import numpy as np
import re


def parse_input(input):
    numbers = list(map(int, list(input[0].split(','))))
    boards = np.array(list(map(lambda x: list(x.split('\n')), input[1:])))
    boards = np.array(list(map(lambda x: np.array(list(map(lambda y: list(map(float, re.split('  | ', y.strip()))), x))), boards)))
    return numbers, boards

def check_board(board):
    for n in range(len(board[0])):
        if np.isnan(board[n]).all():
            return True
        if np.isnan(board[:, n]).all():
            return True
    return False


def part_one(numbers, boards):
    for number in numbers:
        for board in boards:
            board[board == number] = np.nan
            if check_board(board):
                unmarked_sum = np.nansum(board)
                return int(unmarked_sum * number)


def part_two(numbers, boards):
    last_number = 0
    board_indexes = list(np.arange(len(boards)))
    stop_run = False
    for number in numbers:
        if stop_run:
            break
        for index, board in enumerate(boards):
            if index not in board_indexes:
                continue
            board[board == number] = np.nan
            if check_board(board):
                if len(board_indexes) == 1:
                    last_number = number
                    stop_run = True
                    break
                board_indexes.remove(index)

    board = boards[board_indexes[0]]
    unmarked_sum = np.nansum(board)
    return int(unmarked_sum * last_number)


raw_input = helpers.load_puzzle_raw(4)
input = list(raw_input.text.split("\n\n"))
input.pop()
numbers, boards = parse_input(input)
print('Part one result: %s' % (helpers.run_and_time(part_one, numbers, boards)))
print('Part two result: %s' % (helpers.run_and_time(part_two, numbers, boards)))