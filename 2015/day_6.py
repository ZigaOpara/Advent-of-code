import helpers
import numpy as np


def part_one(puzzle_input):
    grid = np.zeros((1000, 1000))
    for instruction in puzzle_input:
        command, p1, p2 = instruction
        if command == 'on':
            grid[p1[0]:p2[0]+1, p1[1]:p2[1]+1] = 1
        elif command == 'off':
            grid[p1[0]:p2[0]+1, p1[1]:p2[1]+1] = 0
        else:
            grid[p1[0]:p2[0]+1, p1[1]:p2[1]+1] = (grid[p1[0]:p2[0]+1, p1[1]:p2[1]+1] + 1) % 2
    return int(grid.sum())


def part_two(puzzle_input):
    grid = np.zeros((1000, 1000))
    for instruction in puzzle_input:
        command, p1, p2 = instruction
        if command == 'on':
            grid[p1[0]:p2[0] + 1, p1[1]:p2[1] + 1] += 1
        elif command == 'off':
            grid[p1[0]:p2[0] + 1, p1[1]:p2[1] + 1] -= 1
            grid[grid < 0] = 0
        else:
            grid[p1[0]:p2[0] + 1, p1[1]:p2[1] + 1] += 2
    return int(grid.sum())


loaded_puzzle_input = helpers.load_puzzle_input(2015, 6)
parsed = [x.split() for x in loaded_puzzle_input]
parsed = [x[1:] if x[0] == 'turn' else x for x in parsed]
parsed = [(x[0], (tuple(map(int, x[1].split(',')))), (tuple(map(int, x[3].split(','))))) for x in parsed]
print('Part one result: %s' % (helpers.run_and_time(part_one, parsed)))
print('Part two result: %s' % (helpers.run_and_time(part_two, parsed)))
