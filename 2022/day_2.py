import helpers

choice_scores = {'X': 1, 'Y': 2, 'Z': 3}


def part_one(puzzle_input):
    score = 0
    for game in puzzle_input:
        score += choice_scores[game[1]]
        if game in (('A', 'X'), ('B', 'Y'), ('C', 'Z')):
            score += 3
        elif game in (('A', 'Y'), ('B', 'Z'), ('C', 'X')):
            score += 6
    return score


def part_two(puzzle_input):
    score = 0
    choice = {'X': {'A': 3, 'B': 1, 'C': 2}, 'Y': {'A': 1, 'B': 2, 'C': 3}, 'Z': {'A': 2, 'B': 3, 'C': 1}}
    for game in puzzle_input:
        if game[1] == 'X':
            score += choice['X'][game[0]]
        elif game[1] == 'Y':
            score += choice['Y'][game[0]] + 3
        elif game[1] == 'Z':
            score += choice['Z'][game[0]] + 6
    return score


loaded_puzzle_input = helpers.load_puzzle_input(2022, 2)
parsed = [(x[0], x[1]) for x in map(lambda x: x.split(' '), loaded_puzzle_input)]
print('Part one result: %s' % (helpers.run_and_time(part_one, parsed)))
print('Part two result: %s' % (helpers.run_and_time(part_two, parsed)))
