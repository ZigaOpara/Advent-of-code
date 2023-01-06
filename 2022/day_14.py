import numpy as np

import helpers


def generate_cave(puzzle_input, draw_line=False):
    parsed = [[list(map(int, t)) for t in list(map(lambda x: list(x.split(',')), l))] for l in
              list(map(lambda x: x.split(' -> '), puzzle_input))]
    flat = [pair for path in parsed for pair in path]
    x_coords, y_coords = [pair[0] for pair in flat], [pair[1] for pair in flat]
    min_x, max_x, max_y = min(x_coords), max(x_coords), max(y_coords)
    if draw_line:
        max_y += 2
        min_x -= 200
        max_x += 200
    cave = np.full((max_y + 1, max_x - min_x + 1), '.')
    if draw_line:
        cave[-1, :] = '#'
    for path in parsed:
        path[0][0] -= min_x
        for i in range(len(path) - 1):
            path[i + 1][0] -= min_x
            if path[i][1] == path[i + 1][1]:
                if path[i][0] < path[i + 1][0]:
                    cave[path[i][1], path[i][0]:path[i + 1][0] + 1] = '#'
                else:
                    cave[path[i][1], path[i + 1][0]:path[i][0] + 1] = '#'
            else:
                if path[i][1] < path[i + 1][1]:
                    cave[path[i][1]:path[i + 1][1] + 1, path[i][0]] = '#'
                else:
                    cave[path[i + 1][1]:path[i][1] + 1, path[i + 1][0]] = '#'
    start = 500 - min_x
    return cave, start


def move_sand(cave, sand, check_start=False):
    initial_sand = sand
    down = (sand[0] + 1, sand[1])
    left = (sand[0] + 1, sand[1] - 1)
    right = (sand[0] + 1, sand[1] + 1)
    try:
        if cave[down] == '.':
            sand = down
            cave[down] = 'o'
        elif cave[left] == '.':
            sand = left
            cave[left] = 'o'
        elif cave[right] == '.':
            sand = right
            cave[right] = 'o'
        else:
            if check_start and sand[0] == 0:
                raise IndexError
            return cave, None
    except IndexError as e:
        raise e
    cave[initial_sand] = '.'
    return cave, sand


def drop_sand(cave, start, check_start=False):
    units = 0
    while True:
        sand = (0, start)
        try:
            cave, sand = move_sand(cave, sand, check_start)
        except IndexError:
            return units + 1 if check_start else 0
        while True:
            try:
                cave, sand = move_sand(cave, sand)
                if sand is None:
                    break
            except IndexError:
                return units
        units += 1


def part_one(puzzle_input):
    cave, start = generate_cave(puzzle_input)
    return drop_sand(cave, start)


def part_two(puzzle_input):
    cave, start = generate_cave(puzzle_input, True)
    return drop_sand(cave, start, True)


loaded_puzzle_input = helpers.load_puzzle_input(2022, 15)
print('Part one result: %s' % (helpers.run_and_time(part_one, loaded_puzzle_input)))
print('Part two result: %s' % (helpers.run_and_time(part_two, loaded_puzzle_input)))
