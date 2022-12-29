import helpers

desired_attributes = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}


def part_one(puzzle_input):
    for sue, attributes in puzzle_input.items():
        comparison = [value == desired_attributes[attribute] for attribute, value in attributes.items()]
        if all(comparison):
            return sue


def part_two(puzzle_input):
    for sue, attributes in puzzle_input.items():
        comparison = []
        for attribute, value in attributes.items():
            if attribute in ['cats', 'trees']:
                comparison.append(value > desired_attributes[attribute])
            elif attribute in ['pomeranians', 'goldfish']:
                comparison.append(value < desired_attributes[attribute])
            else:
                comparison.append(value == desired_attributes[attribute])
        if all(comparison):
            return sue


loaded_puzzle_input = helpers.load_puzzle_input(2015, 16)
parsed = {x[0][4:]: {y[0]: int(y[1]) for y in list(map(lambda x: x.split(': '), (': '.join(x[1:])).split(', ')))} for x
          in list(map(lambda x: x.split(': '), loaded_puzzle_input))}
print('Part one result: %s' % (helpers.run_and_time(part_one, parsed)))
print('Part two result: %s' % (helpers.run_and_time(part_two, parsed)))
