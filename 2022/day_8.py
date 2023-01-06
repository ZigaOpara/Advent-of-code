import numpy

import helpers


def check_line(height, line):
    distance = 0
    for tree in line:
        distance += 1
        if tree >= height:
            return distance
    return distance


def get_scenic_score(r, c, trees, rows, cols):
    if r in [0, rows] or c in [0, cols]:
        return 0
    up = trees[:r, c][::-1]
    down = trees[r+1:, c]
    left = trees[r, :c][::-1]
    right = trees[r, c+1:]
    return numpy.prod(list(map(lambda x: check_line(trees[r, c], x), [up, down, left, right])))


def part_one(puzzle_input):
    visible = numpy.zeros_like(puzzle_input)
    rows, cols = puzzle_input.shape
    for (r, c), value in numpy.ndenumerate(puzzle_input):
        if r in [0, cols - 1] \
                or c in [0, rows - 1] \
                or max(puzzle_input[r, :c]) < value \
                or max(puzzle_input[r, c + 1:]) < value \
                or max(puzzle_input[:r, c]) < value \
                or max(puzzle_input[r + 1:, c]) < value:
            visible[r, c] = 1
    return visible.sum()


def part_two(puzzle_input):
    scenic_scores = numpy.zeros_like(puzzle_input)
    rows, cols = puzzle_input.shape
    for (r, c), value in numpy.ndenumerate(puzzle_input):
        scenic_scores[r, c] = get_scenic_score(r, c, puzzle_input, rows, cols)
    return numpy.amax(scenic_scores)


loaded_puzzle_input = helpers.load_puzzle_input(2022, 8)
parsed = numpy.array([[int(x) for x in y] for y in loaded_puzzle_input])
print('Part one result: %s' % (helpers.run_and_time(part_one, parsed)))
print('Part two result: %s' % (helpers.run_and_time(part_two, parsed)))
