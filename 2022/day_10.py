import helpers


def part_one(puzzle_input):
    cycle, i, x = 1, 0, 1
    strengths = []
    while cycle <= 220:
        if puzzle_input[i][0] == 'noop':
            cycle += 1
        else:
            cycle += 1
            if cycle in [20, 60, 100, 140, 180, 220]:
                strengths.append(x * cycle)
            cycle += 1
            x += puzzle_input[i][1]
        if cycle in [20, 60, 100, 140, 180, 220]:
            strengths.append(x * cycle)
        i += 1
    return sum(strengths)


def part_two(puzzle_input):
    cycle = 0
    i = 0
    sprite_position = 1
    buffer_command = None
    screen = ['', '', '', '', '', '']
    while i < len(puzzle_input):
        screen[cycle // 40] += '#' if cycle % 40 in [sprite_position - 1, sprite_position, sprite_position + 1] else '.'
        if puzzle_input[i][0] == 'addx':
            if not buffer_command:
                buffer_command = puzzle_input[i][1]
            else:
                sprite_position += buffer_command
                buffer_command = None
                i += 1
        else:
            i += 1
        cycle += 1
    return '\n' + '\n'.join(screen)


loaded_puzzle_input = helpers.load_puzzle_input(2022, 10)
parsed = [[x[0], int(x[1])] if len(x) == 2 else x for x in list(map(lambda x: x.split(' '), loaded_puzzle_input))]
print('Part one result: %s' % (helpers.run_and_time(part_one, parsed)))
print('Part two result: %s' % (helpers.run_and_time(part_two, parsed)))
