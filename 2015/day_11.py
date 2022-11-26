import helpers


def is_valid_password(password):
    if any([char in password for char in ['i', 'o', 'l']]):
        return False
    if not any([ord(password[i]) == ord(password[i + 1]) - 1 == ord(password[i + 2]) - 2 for i in
                range(len(password) - 2)]):
        return False
    n_of_pairs = 0
    last_char = password[0]
    for char in password[1:]:
        if char == last_char:
            n_of_pairs += 1
            last_char = '0'
        else:
            last_char = char
    return n_of_pairs > 1


def increment_password(password):
    password = list(password)
    for i in range(1, len(password) + 1):
        new_ord = ord(password[-i]) + 1
        if new_ord <= 122:
            password[-i] = chr(new_ord)
            break
        else:
            password[-i] = 'a'
    return ''.join(password)


def part_one(puzzle_input):
    password = increment_password(puzzle_input)
    while not is_valid_password(password):
        password = increment_password(password)
    return password


def part_two(puzzle_input):
    password = increment_password(puzzle_input)
    while not is_valid_password(password):
        password = increment_password(password)
    password = increment_password(password)
    while not is_valid_password(password):
        password = increment_password(password)
    return password


loaded_puzzle_input = helpers.load_puzzle_input(2015, 11)
parsed = loaded_puzzle_input[0]
print('Part one result: %s' % (helpers.run_and_time(part_one, parsed)))
print('Part two result: %s' % (helpers.run_and_time(part_two, parsed)))
