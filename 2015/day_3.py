import helpers


def part_one(puzzle_input):
    x, y, houses = 0, 0, [(0, 0)]
    for direction in puzzle_input:
        x, y = get_position(direction, x, y)
        if (x, y) not in houses:
            houses.append((x, y))
    return len(houses)


def part_two(puzzle_input):
    xs, ys, xr, yr, houses = 0, 0, 0, 0, [(0, 0)]
    for index, direction in enumerate(puzzle_input):
        if index % 2 == 0:
            xs, ys = get_position(direction, xs, ys)
            if (xs, ys) not in houses:
                houses.append((xs, ys))
        else:
            xr, yr = get_position(direction, xr, yr)
            if (xr, yr) not in houses:
                houses.append((xr, yr))
    return len(houses)


def get_position(direction, x, y):
    if direction == '^':
        y += 1
    elif direction == 'v':
        y -= 1
    elif direction == '>':
        x += 1
    elif direction == '<':
        x -= 1
    return x, y


loaded_puzzle_input = helpers.load_puzzle_raw(2015, 3).text
print('Part one result: %s' % (helpers.run_and_time(part_one, loaded_puzzle_input)))
print('Part two result: %s' % (helpers.run_and_time(part_two, loaded_puzzle_input)))
