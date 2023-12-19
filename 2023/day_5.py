import math

import helpers


def evaluate_map(mappings, source):
    for mapping in mappings:
        if source < mapping[1]:
            continue
        if source >= mapping[1] + mapping[2]:
            continue
        diff = source - mapping[1]
        return mapping[0] + diff
    return source


def evaluate(item_range, mappings):
    item_ranges = []
    range_start, range_length = item_range
    for mapping in mappings:
        mapping_dest, mapping_source, mapping_length = mapping
        split_ranges = split_range(item_range, (mapping_source, mapping_length))
        if len(split_ranges) == 0:
            continue
        elif len(split_ranges) == 1:
            return [(range_start + mapping_dest - mapping_source, range_length)]
        else:
            for r in split_ranges:
                item_ranges += evaluate(r, mappings)
            return item_ranges
    return [item_range]

def split_range(item_range, mapping):
    range_start, range_length = item_range
    mapping_start, mapping_length = mapping
    splits = []

    if range_start < mapping_start <= range_start + range_length - 1:
        sticking_out = mapping_start - range_start
        splits.append((range_start, sticking_out))
        range_start = range_start + sticking_out
        range_length = range_length - sticking_out
    if range_start <= mapping_start + mapping_length - 1 < range_start + range_length - 1:
        sticking_out = range_length - (mapping_start + mapping_length - range_start)
        splits.append((mapping_start + mapping_length, sticking_out))
        range_length = range_length - sticking_out
    if mapping_start <= range_start <= range_start + range_length <= mapping_start + mapping_length:
        splits.append((range_start, range_length))
    return splits


def part_one(puzzle_input):
    evaluations = {}
    for seed in puzzle_input['seeds']:
        evaluations[seed] = {'seed': seed}
        for key, value in puzzle_input.items():
            if key == 'seeds':
                continue
            evaluations[seed][key] = evaluate_map(value, list(evaluations[seed].values())[-1])
    lowest_location_number = math.inf
    for evaluation in evaluations.values():
        if evaluation['humidity-to-location'] < lowest_location_number:
            lowest_location_number = evaluation['humidity-to-location']
    return lowest_location_number


def part_two(puzzle_input):
    seed_ranges = []
    for i in range(0, len(puzzle_input['seeds']), 2):
        seed_ranges.append((puzzle_input['seeds'][i], puzzle_input['seeds'][i+1]))
    evaluations = []
    for seed_range in seed_ranges:
        current_evaluations = [seed_range]
        for key, value in puzzle_input.items():
            if key == 'seeds':
                continue
            seed_evaluations = []
            for evaluation in current_evaluations:
                seed_evaluations += evaluate(evaluation, value)
            current_evaluations = seed_evaluations
        evaluations += current_evaluations
    return min([e[0] for e in evaluations])


loaded_puzzle_input = helpers.load_puzzle_input(2023, 5)
# loaded_puzzle_input = helpers.load_test_puzzle_input()
parsed = {'seeds': list(map(int, loaded_puzzle_input[0].split(': ')[1].split(' ')))}
destination = ''
for line in loaded_puzzle_input[2:]:
    if line == '':
        continue
    if line[0].isdigit():
        parsed.setdefault(destination, []).append(tuple(int(x) for x in line.split(' ')))
    else:
        destination = line.split(' ')[0]
print('Part one result: %s' % (helpers.run_and_time(part_one, parsed)))
print('Part two result: %s' % (helpers.run_and_time(part_two, parsed)))