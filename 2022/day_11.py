import math

import helpers


def calculate_monkey_business(monkeys, rounds, relief):
    lcm = math.prod([x['Test'] for x in monkeys.values()])
    for x in range(rounds):
        for key, value in monkeys.items():
            for _ in range(len(value['Starting items'])):
                value['total'] += 1
                item = value['Starting items'].pop(0)
                item %= lcm
                item = eval(value['Operation'], {'old': item})
                if relief:
                    item //= 3
                monkeys['Monkey {0}'.format(value['If true' if item % value['Test'] == 0 else 'If false'])][
                    'Starting items'].append(item)
    totals = sorted([x['total'] for x in monkeys.values()], reverse=True)
    return totals[0] * totals[1]


def part_one(puzzle_input):
    return calculate_monkey_business(puzzle_input, 20, True)


def part_two(puzzle_input):
    return calculate_monkey_business(puzzle_input, 10000, False)


loaded_puzzle_input = helpers.load_puzzle_input(2022, 11)
parsed = [loaded_puzzle_input[x * 7:(x + 1) * 7 - 1] for x in range(8)]
parsed = {x[0][:-1]: {y[0]: y[1] for y in list(map(lambda x: x.strip().split(': '), x[1:]))} for x in parsed}
for monkey in parsed.values():
    monkey['Starting items'] = list(map(int, monkey['Starting items'].split(', ')))
    monkey['Operation'] = monkey['Operation'].split(' = ')[1]
    monkey['Test'] = int(monkey['Test'].split(' ')[-1])
    monkey['If true'] = int(monkey['If true'].split(' ')[-1])
    monkey['If false'] = int(monkey['If false'].split(' ')[-1])
    monkey['total'] = 0
print('Part one result: %s' % (helpers.run_and_time(part_one, parsed)))
print('Part two result: %s' % (helpers.run_and_time(part_two, parsed)))
