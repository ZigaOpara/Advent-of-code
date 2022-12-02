import itertools

import helpers


def part_one(puzzle_input):
    max_calories = 0
    for group in puzzle_input:
        max_calories = max(sum(group), max_calories)
    return max_calories


def part_two(puzzle_input):
    calories = sorted([sum(group) for group in puzzle_input])
    return sum(calories[-3:])


loaded_puzzle_input = helpers.load_puzzle_input(2022, 1)
parsed = [list(map(int, list(group))) for k, group in itertools.groupby(loaded_puzzle_input, bool) if k]
print('Part one result: %s' % (helpers.run_and_time(part_one, parsed)))
print('Part two result: %s' % (helpers.run_and_time(part_two, parsed)))
