import helpers

def create_paths(input, max_occurrences):
    paths = [['start']]
    while any([path for path in paths if path[-1] != 'end']):
        for path in [path for path in paths if path[-1] != 'end']:
            multiple_used = any([element for element in path if element.islower() and path.count(element) >= max_occurrences])
            available_options = list(
                set(input[path[-1]]) - 
                set([element for element in path if element.islower() and multiple_used or element == 'start']))
            if len(available_options) == 0:
                paths.remove(path)
                continue
            for index, option in enumerate(available_options):
                if index == 0:
                    path.append(option)
                else:
                    new_path = path.copy()
                    new_path[-1] = option
                    paths.append(new_path)
    return len(paths)


def part_one(input):
    paths = create_paths(input, 0)
    print(paths)


def part_two(input):
    paths = create_paths(input, 2)
    print(paths)


input = helpers.load_puzzle_input(12)
input = list(map(lambda x: x.split('-'), input))
input_parsed = {}
for pair in input:
    if pair[0] not in input_parsed.keys():
        input_parsed[pair[0]] = [pair[1]]
    else:
        input_parsed[pair[0]].append(pair[1])
    if pair[1] not in input_parsed.keys():
        input_parsed[pair[1]] = [pair[0]]
    else:
        input_parsed[pair[1]].append(pair[0])
test_input = {
    'start': ['A', 'b'],
    'end': ['A', 'b'],
    'A': ['start', 'end', 'b', 'c'],
    'b': ['start', 'end', 'A', 'd'],
    'c': ['A'],
    'd': ['b']
}

test_input_2 = {
    'start': ['HN', 'dc', 'kj'],
    'end': ['dc', 'HN'],
    'dc': ['start', 'end', 'HN', 'LN', 'kj'],
    'HN': ['start', 'end', 'dc', 'kj'],
    'kj': ['sa', 'HN', 'dc', 'start'],
    'LN': ['dc'],
    'sa': ['kj']
}

print('Part one result: %s' % (helpers.run_and_time(part_one, input_parsed)))
print('Part two result: %s' % (helpers.run_and_time(part_two, input_parsed)))