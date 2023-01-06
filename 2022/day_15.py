import numpy as np

import helpers


def draw_area(field, center, radius):
    field[center[0]-radius:center[0]+radius, center[1]-radius:center[1]+radius] = '#'
    print(field)


# def part_one(puzzle_input):
#     cave, start = generate_cave(puzzle_input)
#     return drop_sand(cave, start)


# def part_two(puzzle_input):
#     cave, start = generate_cave(puzzle_input, True)
#     return drop_sand(cave, start, True)


loaded_puzzle_input = helpers.load_puzzle_input(2022, 15)
loaded_puzzle_input = helpers.load_test_puzzle_input()
tmp = np.full((10, 10), '.')
draw_area(tmp, (3,5), 2)

# print('Part one result: %s' % (helpers.run_and_time(part_one, loaded_puzzle_input)))
# print('Part two result: %s' % (helpers.run_and_time(part_two, loaded_puzzle_input)))
