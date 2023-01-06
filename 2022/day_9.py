import numpy

import helpers


def move_head(direction, h):
    if direction == 'U':
        h[0] -= 1
    elif direction == 'D':
        h[0] += 1
    elif direction == 'L':
        h[1] -= 1
    else:
        h[1] += 1
    return h


def follow(current, lead):
    if abs(lead[0] - current[0]) > 1 or abs(lead[1] - current[1]) > 1:
        if current[0] < lead[0]:
            current[0] += 1
        elif current[0] > lead[0]:
            current[0] -= 1

        if current[1] < lead[1]:
            current[1] += 1
        elif current[1] > lead[1]:
            current[1] -= 1
    return current


def part_one(puzzle_input):
    field = numpy.zeros([1000, 1000])
    h, t = [500, 500], [500, 500]
    field[tuple(t)] = 1
    for motion in puzzle_input:
        for i in range(motion[1]):
            h = move_head(motion[0], h)
            t = follow(t, h)
            field[tuple(t)] = 1
    return int(field.sum())


def part_two(puzzle_input):
    field = numpy.zeros([1000, 1000])
    knots = numpy.full((10, 2), [500, 500])
    field[tuple(knots[-1])] = 1
    for motion in puzzle_input:
        for i in range(motion[1]):
            knots[0] = move_head(motion[0], knots[0])
            for j in range(1, len(knots)):
                knots[j] = follow(knots[j], knots[j - 1])
            field[tuple(knots[-1])] = 1
    return int(field.sum())


loaded_puzzle_input = helpers.load_puzzle_input(2022, 9)
parsed = [(x[0], int(x[1])) for x in list(map(lambda x: x.split(' '), loaded_puzzle_input))]
print('Part one result: %s' % (helpers.run_and_time(part_one, parsed)))
print('Part two result: %s' % (helpers.run_and_time(part_two, parsed)))
