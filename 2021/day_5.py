import helpers
import numpy as np

def consider_vertical_and_horizontal(board, x1, x2, y1, y2):
    if x1 == x2:
        if y1 < y2:
            board[y1:y2+1, x1] += 1
        else:
            board[y2:y1+1, x1] += 1
    else:
        if x1 < x2:
            board[y1, x1:x2+1] += 1
        else:
            board[y1, x2:x1+1] += 1


def consider_diagonal(board, x1, x2, y1, y2):
    range_x = range(x1, x2+1) if x1 < x2 else range(x1, x2-1, -1)
    range_y = range(y1, y2+1) if y1 < y2 else range(y1, y2-1, -1)
    for x, y in zip(range_x, range_y):
        board[y, x] += 1


def part_one(input):
    board = np.zeros((1000, 1000))
    for line in input:
        x1, y1, x2, y2 = line[0][0], line[0][1], line[1][0], line[1][1]
        if x1 == x2 or y1 == y2:
            consider_vertical_and_horizontal(board, x1, x2, y1, y2)

    result = (board >= 2).sum()
    return result


def part_two(input):
    board = np.zeros((1000, 1000))
    for line in input:
        x1, y1, x2, y2 = line[0][0], line[0][1], line[1][0], line[1][1]
        if x1 == x2 or y1 == y2:
            consider_vertical_and_horizontal(board, x1, x2, y1, y2)
        else:
            consider_diagonal(board, x1, x2, y1, y2)
    
    result = (board >= 2).sum()
    return result

input = helpers.load_puzzle_input(5)
input = list(map(lambda x: x.split(' -> '), input))
input = np.array(list(map(lambda x: list(map(lambda y: list(map(int, y.split(','))), x)), input)))
print('Part one result: %s' % (helpers.run_and_time(part_one, input)))
print('Part two result: %s' % (helpers.run_and_time(part_two, input)))