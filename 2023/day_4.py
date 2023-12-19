import helpers


def part_one(puzzle_input):
    points = 0
    for line in puzzle_input.values():
        points += int(pow(2, len(set(line[0]).intersection(set(line[1]))) - 1))
    return points


def part_two(puzzle_input):
    cards = {x + 1: 1 for x in range(len(puzzle_input))}
    for key, value in puzzle_input.items():
        matches = len(set(value[0]).intersection(set(value[1])))
        for i in range(matches):
            cards[key + i + 1] += cards[key]
    return sum(cards.values())


loaded_puzzle_input = helpers.load_puzzle_input(2023, 4)
parsed = {int(x[0].split(' ')[-1]): [[int(z) for z in y.split(' ') if z != ''] for y in x[1].split(' | ')] for x in map(lambda line: line.split(': '), loaded_puzzle_input)}
print('Part one result: %s' % (helpers.run_and_time(part_one, parsed)))
print('Part two result: %s' % (helpers.run_and_time(part_two, parsed)))