import helpers

def part_one(input):
    horizontal = 0
    vertical = 0
    for command in input:
        if command.startswith('forward'):
            amount = int(command[8:])
            horizontal += amount
        if command.startswith('down'):
            amount = int(command[5:])
            vertical += amount
        if command.startswith('up'):
            amount = int(command[3:])
            vertical -= amount
    result = horizontal * vertical
    return result


def part_two(input):
    horizontal = 0
    vertical = 0
    aim = 0
    for command in input:
        if command.startswith('forward'):
            amount = int(command[8:])
            horizontal += amount
            vertical += amount * aim
        if command.startswith('down'):
            amount = int(command[5:])
            aim += amount
        if command.startswith('up'):
            amount = int(command[3:])
            aim -= amount
    result = horizontal * vertical
    return result

input = helpers.load_puzzle_input(2021, 2)

print('Part one result: %s' % (helpers.run_and_time(part_one, input)))
print('Part two result: %s' % (helpers.run_and_time(part_two, input)))