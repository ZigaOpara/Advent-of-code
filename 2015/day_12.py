import json
import re

import helpers


def remove_red(element):
    if isinstance(element, str) or isinstance(element, int):
        return element
    if isinstance(element, dict):
        if 'red' in element.values():
            return {}
        for key, value in element.items():
            element[key] = remove_red(value)
        return element
    if isinstance(element, list):
        for index, value in enumerate(element):
            element[index] = remove_red(value)
        return element


def part_one(puzzle_input):
    matches = re.findall(r'-?[0-9]\d*', puzzle_input)
    return sum(map(lambda x: int(x), matches))


def part_two(puzzle_input):
    parsed = json.loads(puzzle_input)
    no_red = remove_red(parsed)
    serialized = json.dumps(no_red)
    matches = re.findall(r'-?[0-9]\d*', serialized)
    return sum(map(lambda x: int(x), matches))


loaded_puzzle_input = helpers.load_puzzle_input(2015, 12)
print('Part one result: %s' % (helpers.run_and_time(part_one, loaded_puzzle_input[0])))
print('Part two result: %s' % (helpers.run_and_time(part_two, loaded_puzzle_input[0])))
