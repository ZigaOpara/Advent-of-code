import itertools

import helpers


def evaluate_relationships(seating_order, relationships):
    happiness = 0
    for i in range(-1, len(seating_order) - 1):
        if 'Me' in [seating_order[i], seating_order[i + 1]]:
            continue
        happiness += relationships[seating_order[i]][seating_order[i + 1]]
        happiness += relationships[seating_order[i + 1]][seating_order[i]]
    return happiness


def part_one(puzzle_input):
    knights = puzzle_input.keys()
    best_happiness = 0
    for permutation in list(itertools.permutations(knights)):
        best_happiness = max(evaluate_relationships(permutation, puzzle_input), best_happiness)
    return best_happiness


def part_two(puzzle_input):
    knights = list(puzzle_input.keys())
    knights.append('Me')
    best_happiness = 0
    for permutation in list(itertools.permutations(knights)):
        best_happiness = max(evaluate_relationships(permutation, puzzle_input), best_happiness)
    return best_happiness


loaded_puzzle_input = helpers.load_puzzle_input(2015, 13)
parsed = [(x[0], x[10], int(x[3]) if x[2] == 'gain' else -int(x[3])) for x in
          (y[:-1].split(' ') for y in loaded_puzzle_input)]
relationship_dict = {}
for line in parsed:
    relationship_dict.setdefault(line[0], {})[line[1]] = line[2]
print('Part one result: %s' % (helpers.run_and_time(part_one, relationship_dict)))
print('Part two result: %s' % (helpers.run_and_time(part_two, relationship_dict)))
