import itertools
import sys

import helpers


def generate_adjacency_dict(puzzle_input):
    adjacency_dict = {}
    for item in puzzle_input:
        adjacency_dict.setdefault(item[0], {})[item[1]] = item[2]
        adjacency_dict.setdefault(item[1], {})[item[0]] = item[2]
    return adjacency_dict


def part_one(adjacency_dict):
    cities = list(adjacency_dict.keys())

    shortest_path = sys.maxsize
    for permutation in list(itertools.permutations(cities)):
        path = sum(map(lambda x, y: adjacency_dict[x][y], permutation[:-1], permutation[1:]))
        shortest_path = min(shortest_path, path)
    return shortest_path


def part_two(adjacency_dict):
    cities = list(adjacency_dict.keys())

    longest_path = 0
    for permutation in list(itertools.permutations(cities)):
        path = sum(map(lambda x, y: adjacency_dict[x][y], permutation[:-1], permutation[1:]))
        longest_path = max(longest_path, path)
    return longest_path


loaded_puzzle_input = helpers.load_puzzle_input(2015, 9)
parsed = [(x[0], x[2], int(x[4])) for x in (y.split(' ') for y in loaded_puzzle_input)]
adjacency = generate_adjacency_dict(parsed)
print('Part one result: %s' % (helpers.run_and_time(part_one, adjacency)))
print('Part two result: %s' % (helpers.run_and_time(part_two, adjacency)))
