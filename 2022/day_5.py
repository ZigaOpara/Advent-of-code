import copy

import helpers


def part_one(arrangement, instructions):
    for move in instructions:
        for i in range(move[0]):
            arrangement[move[2]].insert(0, arrangement[move[1]].pop(0))
    return ''.join([arrangement[key][0] for key in range(1, len(arrangement.keys()) + 1)])


def part_two(arrangement, instructions):
    for move in instructions:
        arrangement[move[2]] = arrangement[move[1]][:move[0]] + arrangement[move[2]]
        arrangement[move[1]] = arrangement[move[1]][move[0]:]
    return ''.join([arrangement[key][0] for key in range(1, len(arrangement.keys()) + 1)])


loaded_puzzle_input = helpers.load_puzzle_input(2022, 5)
empty_line = loaded_puzzle_input.index('')
containers = {}
for line in loaded_puzzle_input[:empty_line-1]:
    x = 0
    while x < len(line):
        if line[x:x + 4][1] != ' ':
            containers.setdefault(x//4 + 1, []).append(line[x:x+4][1])
        x += 4
procedure = [(int(x[1]), int(x[3]), int(x[5])) for x in map(lambda y: y.split(' '), loaded_puzzle_input[empty_line+1:])]
print('Part one result: %s' % (helpers.run_and_time(part_one, copy.deepcopy(containers), procedure)))
print('Part two result: %s' % (helpers.run_and_time(part_two, containers, procedure)))
