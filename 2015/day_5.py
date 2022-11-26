import helpers


def part_one(puzzle_input):
    banned_strings = ['ab', 'cd', 'pq', 'xy']
    nice = 0
    for string in puzzle_input:
        if check_for_vowels(string) and check_for_double(string) and not any(x in string for x in banned_strings):
            nice += 1
    return nice


def part_two(puzzle_input):
    nice = 0
    for string in puzzle_input:
        if check_for_repeating_pair(string) and check_for_repeat(string):
            nice += 1
    return nice


def check_for_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    n_of_vowels = 0
    for char in string:
        if char in vowels:
            n_of_vowels += 1
    return n_of_vowels >= 3


def check_for_double(string):
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            return True
    return False


def check_for_repeating_pair(string):
    for i in range(len(string) - 1):
        if string[i:i + 2] in string[i + 2:]:
            return True
    return False


def check_for_repeat(string):
    for i in range(len(string) - 2):
        if string[i] == string[i + 2]:
            return True
    return False


loaded_puzzle_input = helpers.load_puzzle_input(2015, 5)
print('Part one result: %s' % (helpers.run_and_time(part_one, loaded_puzzle_input)))
print('Part two result: %s' % (helpers.run_and_time(part_two, loaded_puzzle_input)))
