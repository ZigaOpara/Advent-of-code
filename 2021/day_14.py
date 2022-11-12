import helpers
import collections

def process_step(template, rules):
    result = template[0]
    for index, char in enumerate(list(template)):
        if index == 0:
            continue
        pair = template[index-1] + char
        if pair in rules.keys():
            result += rules[pair]
        result += char
    return result


def part_one(template, rules):
    for i in range(10):
        template = process_step(template, rules)
    counted = collections.Counter(template).most_common()
    return counted[0][1] - counted[-1][1]


def part_two(template, rules):
    for i in range(40):
        print(i)
        template = process_step(template, rules)
    counted = collections.Counter(template).most_common()
    return counted[0][1] - counted[-1][1]


input = helpers.load_puzzle_input(2021, 14)
template = input[0]
rules = input[2:]
rules = list(map(lambda x: x.split(' -> '), rules))
rules = { x[0]: x[1] for x in rules }
test_template = 'NNCB'
test_rules = {
    'CH': 'B',
    'HH': 'N',
    'CB': 'H',
    'NH': 'C',
    'HB': 'C',
    'HC': 'B',
    'HN': 'C',
    'NN': 'C',
    'BH': 'H',
    'NC': 'B',
    'NB': 'B',
    'BN': 'B',
    'BB': 'N',
    'BC': 'B',
    'CC': 'N',
    'CN': 'C',
}
print(part_one(template, rules))
print(part_two(template, rules))