import functools
import itertools

import helpers


def check_order(left, right):
    for l, r in itertools.zip_longest(left, right):
        if isinstance(l, int) and isinstance(r, int):
            if l != r:
                return -1 if l < r else 1
        elif isinstance(l, list) and isinstance(r, list):
            order = check_order(l, r)
            if order != 0:
                return order
        elif l is None and r is not None:
            return -1
        elif l is not None and r is None:
            return 1
        else:
            if isinstance(l, int):
                l = [l]
            else:
                r = [r]
            order = check_order(l, r)
            if order != 0:
                return order
    return 0


def part_one(puzzle_input):
    ordered = []
    for index, pair in enumerate(puzzle_input):
        if check_order(pair[0], pair[1]) == -1:
            ordered.append(index + 1)
    return sum(ordered)


def part_two(puzzle_input):
    s = sorted(puzzle_input, key=functools.cmp_to_key(check_order))
    return (s.index([[2]]) + 1) * (s.index([[6]]) + 1)


loaded_puzzle_input = helpers.load_puzzle_input(2022, 13)
parsed = [(eval(loaded_puzzle_input[x]), eval(loaded_puzzle_input[x + 1])) for x in
          range(0, len(loaded_puzzle_input), 3)]
print('Part one result: %s' % (helpers.run_and_time(part_one, parsed)))
parsed = [eval(x) for x in loaded_puzzle_input if x != ''] + [[[2]], [[6]]]
print('Part two result: %s' % (helpers.run_and_time(part_two, parsed)))
