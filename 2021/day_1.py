import helpers


def part_one(input):
    n_of_increases = 0
    for index, measurment in enumerate(input):
        if index == 0:
            continue
        if measurment > input[index-1]:
            n_of_increases += 1
    return n_of_increases


def part_two(input):
    n_of_increases = 0
    for index, measurment in enumerate(input):
        if index < 3:
            continue
        window_A = sum(input[index-3:index])
        window_B = sum(input[index-2:index+1])
        if window_B > window_A:
            n_of_increases += 1
    return n_of_increases


input = helpers.load_puzzle_input(2021, 1)
parsed = list(map(int, input))
print('Part one result: %s' % (helpers.run_and_time(part_one, parsed)))
print('Part two result: %s' % (helpers.run_and_time(part_two, parsed)))