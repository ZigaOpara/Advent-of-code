import itertools
import sys

import numpy as np
from scipy.spatial.distance import cityblock

import helpers


def cb(v1, v2):
    return cityblock(v1, v2)


def draw_area(field, center, radius):
    for (r, c), value in np.ndenumerate(field):
        if cityblock((r, c), center) <= radius and value == '.':
            field[(r, c)] = '#'
    print(field)


def get_nearest_beacon(sensor, beacons):
    nearest = beacons[0]
    nearest_distance = sys.maxsize
    for beacon in beacons:
        distance = cityblock(sensor, beacon)
        if distance < nearest_distance:
            nearest = beacon
            nearest_distance = distance
    return nearest, nearest_distance


def part_one(puzzle_input):
    x_coords = sorted(list(itertools.chain(*[[x['s'][0], x['b'][0]] for x in puzzle_input])))
    min_x, max_x = x_coords[0]-10, x_coords[-1]+10
    y_coords = sorted(list(itertools.chain(*[[x['s'][1], x['b'][1]] for x in puzzle_input])))
    min_y, max_y = y_coords[0]-10, y_coords[-1]+10
    field = np.full((max_x-min_x+1, max_y-min_y+1), '.')
    for line in puzzle_input:
        line['s'][0] -= min_x
        line['b'][0] -= min_x
        line['s'][1] -= min_y
        line['b'][1] -= min_y
    for line in puzzle_input:
        field[tuple(line['s'])] = 'S'
        field[tuple(line['b'])] = 'B'
    for line in puzzle_input:
        draw_area(field, tuple(line['s']), cityblock(tuple(line['s']), tuple(line['b'])))
    print(np.count_nonzero(field[10-min_y-1] == '#'))


# def part_two(puzzle_input):
#     cave, start = generate_cave(puzzle_input, True)
#     return drop_sand(cave, start, True)


# loaded_puzzle_input = helpers.load_puzzle_input(2022, 15)
loaded_puzzle_input = helpers.load_test_puzzle_input()
parsed = [{'s': [int(x[3][2:-1]), int(x[2][2:-1])], 'b': [int(x[9][2:]), int(x[8][2:-1])]} for x in
          list(map(lambda x: x.split(' '), loaded_puzzle_input))]
print('Part one result: %s' % (helpers.run_and_time(part_one, parsed)))
# print('Part two result: %s' % (helpers.run_and_time(part_two, loaded_puzzle_input)))
