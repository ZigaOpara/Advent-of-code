import helpers


def part_one(puzzle_input):
    floor = 0
    for char in puzzle_input:
        if char == '(':
            floor += 1
        if char == ')':
            floor -= 1
    return floor


def part_two(puzzle_input):
    floor = 0
    for index, char in enumerate(puzzle_input):
        if char == '(':
            floor += 1
        if char == ')':
            floor -= 1
        if floor == -1:
            return index + 1


loaded_puzzle_input = helpers.load_puzzle_raw(2015, 1).text
print('Part one result: %s' % (helpers.run_and_time(part_one, loaded_puzzle_input)))
print('Part two result: %s' % (helpers.run_and_time(part_two, loaded_puzzle_input)))
