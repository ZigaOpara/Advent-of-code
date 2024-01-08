import numpy as np

import helpers


connections = {
    '|': [(-1, 0), (1, 0)],
    '-': [(0, -1), (0, 1)],
    'L': [(-1, 0), (0, 1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(0, -1), (1, 0)],
    'F': [(0, 1), (1, 0)]
}


def part_one(puzzle_input):
    start = np.argwhere(puzzle_input == 'S')[0]
    # find path direction
    for neighbour in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        print(start[0] + neighbour[0], start[1] + neighbour[1])
        neighbour_char = puzzle_input[start[0] + neighbour[0], start[1] + neighbour[1]]
        for connection in connections[neighbour_char]:
            if 'S' in puzzle_input[neighbour[0] + connection[0], neighbour[1] + connection[1]]:
                print(neighbour)
    return


def part_two(puzzle_input):
    return


# loaded_puzzle_input = helpers.load_puzzle_input(2023, 10)
loaded_puzzle_input = helpers.load_test_puzzle_input()
parsed = np.array([list(x) for x in loaded_puzzle_input])
print('Part one result: %s' % (helpers.run_and_time(part_one, parsed)))
print('Part two result: %s' % (helpers.run_and_time(part_two, parsed)))
