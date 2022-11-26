import helpers


def apply_look_and_say(string):
    split_string = list(string)
    temp_res = [[split_string[0]]]
    for char in split_string[1:]:
        if char in temp_res[-1]:
            temp_res[-1].append(char)
        else:
            temp_res.append([char])
    res = ''
    for sequence in temp_res:
        res += str(len(sequence)) + sequence[0]
    return res


def part_one(puzzle_input):
    res = puzzle_input
    for i in range(40):
        res = apply_look_and_say(res)
    return len(res)


def part_two(puzzle_input):
    res = puzzle_input
    for i in range(50):
        res = apply_look_and_say(res)
    return len(res)


loaded_puzzle_input = helpers.load_puzzle_input(2015, 10)
parsed = loaded_puzzle_input[0]
print('Part one result: %s' % (helpers.run_and_time(part_one, parsed)))
print('Part two result: %s' % (helpers.run_and_time(part_two, parsed)))
