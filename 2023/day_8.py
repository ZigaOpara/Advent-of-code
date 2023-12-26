import math

import helpers


def find_path_length(start, endings, instructions, puzzle_input):
    current_node = start
    steps = 0
    while True:
        for instruction in instructions:
            steps += 1
            current_node = puzzle_input[current_node][0 if instruction == 'L' else 1]
            if current_node in endings:
                return steps


def part_one(instructions, puzzle_input):
    return find_path_length('AAA', ['ZZZ'], instructions, puzzle_input)


def part_two(instructions, puzzle_input):
    starting_nodes = [node for node in puzzle_input if node[2] == 'A']
    ending_nodes = [node for node in puzzle_input if node[2] == 'Z']

    path_lengths = []
    for node in starting_nodes:
        path_lengths.append(find_path_length(node, ending_nodes, instructions, puzzle_input))
    return math.lcm(*path_lengths)


loaded_puzzle_input = helpers.load_puzzle_input(2023, 8)
inst = loaded_puzzle_input[0]
parsed = {node[0:3]: (node[7:10], node[12:15]) for node in loaded_puzzle_input[2:]}
print('Part one result: %s' % (helpers.run_and_time(part_one, inst, parsed)))
print('Part two result: %s' % (helpers.run_and_time(part_two, inst, parsed)))