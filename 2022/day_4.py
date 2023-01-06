import re

import helpers


def part_one(puzzle_input):
    overlapping = 0
    for pair in puzzle_input:
        if (pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]) or (
                pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]):
            overlapping += 1
    return overlapping


def part_two(puzzle_input):
    overlapping = 0
    for pair in puzzle_input:
        range_1 = set(range(pair[0][0], pair[0][1] + 1))
        range_2 = set(range(pair[1][0], pair[1][1] + 1))
        if len(range_1.intersection(range_2)) > 0:
            overlapping += 1
    return overlapping


loaded_puzzle_input = helpers.load_puzzle_input(2022, 4)
parsed = [[[x[0], x[1]], [x[2], x[3]]] for x in
          [list(map(int, y)) for y in list(map(lambda x: re.split(r',|-', x), loaded_puzzle_input))]]
print('Part one result: %s' % (helpers.run_and_time(part_one, parsed)))
print('Part two result: %s' % (helpers.run_and_time(part_two, parsed)))
