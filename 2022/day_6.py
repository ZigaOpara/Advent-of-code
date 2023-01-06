import helpers


def detect_distinct_characters(string, number_of_characters):
    for i in range(number_of_characters, len(string)):
        if len(set(string[i - number_of_characters:i])) == number_of_characters:
            return i


def part_one(puzzle_input):
    return detect_distinct_characters(puzzle_input, 4)


def part_two(puzzle_input):
    return detect_distinct_characters(puzzle_input, 14)


loaded_puzzle_input = helpers.load_puzzle_input(2022, 6)
print('Part one result: %s' % (helpers.run_and_time(part_one, loaded_puzzle_input[0])))
print('Part two result: %s' % (helpers.run_and_time(part_two, loaded_puzzle_input[0])))
