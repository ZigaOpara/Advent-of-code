import hashlib

import helpers


def part_one(puzzle_input):
    return get_n_for_hash(puzzle_input, 5)


def part_two(puzzle_input):
    return get_n_for_hash(puzzle_input, 6)


def get_n_for_hash(secret_key, zeroes):
    n = 0
    zeroes_str = '0' * zeroes
    while hashlib.md5((secret_key + str(n)).encode()).hexdigest()[:zeroes] != zeroes_str:
        n += 1
    return n


loaded_puzzle_input = 'bgvyzdsv'
print('Part one result: %s' % (helpers.run_and_time(part_one, loaded_puzzle_input)))
print('Part two result: %s' % (helpers.run_and_time(part_two, loaded_puzzle_input)))
