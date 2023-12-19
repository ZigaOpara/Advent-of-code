import functools

import helpers


def part_one(puzzle_input):
    possible_games = []
    n_cubes = {'red': 12, 'green': 13, 'blue': 14}
    for game, sets in puzzle_input.items():
        possible = True
        for s in sets:
            for color, count in s.items():
                if count > n_cubes[color]:
                    possible = False
                    break
        if possible:
            possible_games.append(game)
    return sum(possible_games)


def part_two(puzzle_input):
    powers = 0
    for game, sets in puzzle_input.items():
        n_cubes = {'red': 0, 'green': 0, 'blue': 0}
        for s in sets:
            for color, count in s.items():
                if count > n_cubes[color]:
                    n_cubes[color] = count
        powers += functools.reduce((lambda x, y: x * y), n_cubes.values())
    return powers


loaded_puzzle_input = helpers.load_puzzle_input(2023, 2)
parsed = {int(x[0].split(' ')[1]): [{z.split(' ')[1]: int(z.split(' ')[0]) for z in y.split(', ')} for y in x[1].split('; ')] for x in map(lambda line: line.split(': '), loaded_puzzle_input)}
print('Part one result: %s' % (helpers.run_and_time(part_one, parsed)))
print('Part two result: %s' % (helpers.run_and_time(part_two, parsed)))