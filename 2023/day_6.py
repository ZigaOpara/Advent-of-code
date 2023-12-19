import math
import re

import helpers


def part_one(puzzle_input):
    puzzle_input = [(int(puzzle_input[0][i]), int(puzzle_input[1][i])) for i in range(len(puzzle_input[0]))]
    res = []
    for race in puzzle_input:
        valid = 0
        for t in range(1, race[0] - 1):
            distance = t * (race[0] - t)
            if distance > race[1]:
                valid += 1
        res.append(valid)
    return math.prod(res)


def part_two(puzzle_input):
    time = int(''.join(puzzle_input[0]))
    record_distance = int(''.join(puzzle_input[1]))
    valid = 0
    for t in range(time):
        distance = t * (time - t)
        if distance > record_distance:
            valid += 1
        elif valid:
            break
    return valid


loaded_puzzle_input = helpers.load_puzzle_input(2023, 6)
# loaded_puzzle_input = helpers.load_test_puzzle_input()
parsed = list(map(lambda x: re.sub(' {2,}', ' ', x).split(' ')[1:], loaded_puzzle_input))
print('Part one result: %s' % (helpers.run_and_time(part_one, parsed)))
print('Part two result: %s' % (helpers.run_and_time(part_two, parsed)))