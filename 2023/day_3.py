import helpers


adjacent_points = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def get_symbol_locations(schematic):
    symbol_locations = []
    for i, line in enumerate(schematic):
        for j, char in enumerate(line):
            if char != '.' and not char.isdigit():
                symbol_locations.append((i, j))
    return symbol_locations

def get_star_locations(schematic):
    start_locations = []
    for i, line in enumerate(schematic):
        for j, char in enumerate(line):
            if char == '*':
                start_locations.append((i, j))
    return start_locations


def get_adjacent_numbers(schematic, symbol_location):
    adjacent_numbers = []
    adjacent_number_points = []
    for point in adjacent_points:
        try:
            if schematic[symbol_location[0] + point[0]][symbol_location[1] + point[1]].isdigit():
                adjacent_number_points.append((symbol_location[0] + point[0], symbol_location[1] + point[1]))
                if (symbol_location[0] + point[0], symbol_location[1] + point[1] + 1) not in adjacent_number_points and not (symbol_location[0] + point[0], symbol_location[1] + point[1] - 1) in adjacent_number_points:
                    adjacent_numbers.append(get_whole_number(schematic, (symbol_location[0] + point[0], symbol_location[1] + point[1])))
                continue
        except IndexError:
            continue
    return adjacent_numbers


def get_whole_number(schematic, digit_location):
    left = ''
    left_index = digit_location[1] - 1
    right = ''
    right_index = digit_location[1] + 1
    while True:
        try:
            char = schematic[digit_location[0]][left_index]
            if char.isdigit():
                left = char + left
            else:
                break
            left_index -= 1
        except IndexError:
            break
    while True:
        try:
            char = schematic[digit_location[0]][right_index]
            if char.isdigit():
                right += char
            else:
                break
        except IndexError:
            break
        right_index += 1
    return int(left + schematic[digit_location[0]][digit_location[1]] + right)


def part_one(puzzle_input):
    part_numbers = []
    symbol_locations = get_symbol_locations(puzzle_input)
    for symbol_location in symbol_locations:
        part_numbers = part_numbers + get_adjacent_numbers(puzzle_input, symbol_location)
    return sum(part_numbers)


def part_two(puzzle_input):
    gear_ratios = []
    star_locations = get_star_locations(puzzle_input)
    for star_location in star_locations:
        adjacent_numbers = get_adjacent_numbers(puzzle_input, star_location)
        if len(adjacent_numbers) != 2:
            continue
        gear_ratios.append(adjacent_numbers[0] * adjacent_numbers[1])
    return sum(gear_ratios)


loaded_puzzle_input = helpers.load_puzzle_input(2023, 3)
print('Part one result: %s' % (helpers.run_and_time(part_one, loaded_puzzle_input)))
print('Part two result: %s' % (helpers.run_and_time(part_two, loaded_puzzle_input)))