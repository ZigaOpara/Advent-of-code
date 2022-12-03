import helpers


def calculate_priority(matches):
    priority = 0
    for char in matches:
        priority += ord(char) - (96 if ord(char) > 96 else 38)
    return priority


def part_one(puzzle_input):
    matches = []
    for string in puzzle_input:
        half = len(string) // 2
        matches += set(string[:half]).intersection(set(string[half:]))
    return calculate_priority(matches)



def part_two(puzzle_input):
    matches = []
    for i in range(0, len(puzzle_input), 3):
        matches += set(puzzle_input[i]).intersection(puzzle_input[i+1]).intersection(puzzle_input[i+2])
    return calculate_priority(matches)


loaded_puzzle_input = helpers.load_puzzle_input(2022, 3)
print('Part one result: %s' % (helpers.run_and_time(part_one, loaded_puzzle_input)))
print('Part two result: %s' % (helpers.run_and_time(part_two, loaded_puzzle_input)))
