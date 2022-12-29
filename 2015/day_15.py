import re

import helpers


def brute_force_recipe(properties, check_calories):
    best_score = 0
    for i in range(100):
        for j in range(100 - i):
            for k in range(100 - i - j):
                l = 100 - i - j - k
                c = i * properties[0][0] + j * properties[1][0] + k * properties[2][0] + l * properties[3][0]
                d = i * properties[0][1] + j * properties[1][1] + k * properties[2][1] + l * properties[3][1]
                f = i * properties[0][2] + j * properties[1][2] + k * properties[2][2] + l * properties[3][2]
                t = i * properties[0][3] + j * properties[1][3] + k * properties[2][3] + l * properties[3][3]
                calories = i * properties[0][4] + j * properties[1][4] + k * properties[2][4] + l * \
                           properties[3][4]
                if any(x <= 0 for x in [c, d, f, t]):
                    continue
                if check_calories and calories != 500:
                    continue
                best_score = max(c * d * f * t, best_score)
    return best_score


def part_one(puzzle_input):
    return brute_force_recipe(puzzle_input, False)


def part_two(puzzle_input):
    return brute_force_recipe(puzzle_input, True)


loaded_puzzle_input = helpers.load_puzzle_input(2015, 15)
parsed = [list(map(int, re.findall(r'-?[0-9]\d*', x))) for x in loaded_puzzle_input]
print('Part one result: %s' % (helpers.run_and_time(part_one, parsed)))
print('Part two result: %s' % (helpers.run_and_time(part_two, parsed)))
