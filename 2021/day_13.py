import helpers
import numpy as np

def fold(dots, fold):
    if fold[0] == 'x':
        for pair in [pair for pair in dots if pair[0] > fold[1]]:
            pair[0] -= 2 * (pair[0]-fold[1])
    else:
        for pair in [pair for pair in dots if pair[1] > fold[1]]:
            pair[1] -= 2 * (pair[1]-fold[1])
    res = []
    [res.append(x) for x in dots if x not in res]
    return res


def visualize(dots):
    max_x = max([element[0] for element in dots])+1
    max_y = max([element[1] for element in dots])+1
    field = np.full((max_y, max_x), '.')
    for dot in dots:
        field[dot[1], dot[0]] = '#'
    field = np.array(list(map(lambda x: ''.join(x), field)))
    print(field)


def part_one(dots, folds):
    folded = fold(dots, folds[0])
    return len(folded)


def part_two(dots, folds):
    for element in folds:
        fold(dots, element)
    visualize(dots)


r = helpers.load_puzzle_raw(13)
input = list(r.text.split("\n\n"))
dots = input[0].split('\n')
dots = list(map(lambda x: list(map(int, x.split(','))), dots))
folds = input[1].split('\n')
folds.pop()
folds = list(map(lambda x: x[11:].split('='), folds))
folds = list(map(lambda x: [x[0], int(x[1])], folds))


test_dots = [
    [6, 10],
    [0, 14],
    [9, 10],
    [0, 3],
    [10, 4],
    [4, 11],
    [6, 0],
    [6, 12],
    [4, 1],
    [0, 13],
    [10, 12],
    [3, 4],
    [3, 0],
    [8, 4],
    [1, 10],
    [2, 14],
    [8, 10],
    [9, 0]
]

test_folds = [
    ['y', 7],
    ['x', 5]
]

print('Part one result: %s'%(helpers.run_and_time(part_one, dots, folds)))
print('Part two result: %s'%(helpers.run_and_time(part_two, dots, folds)))