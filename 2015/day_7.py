import helpers


def part_one(puzzle_input):
    res = calculate_wires(puzzle_input.copy())
    return res['a']


def part_two(puzzle_input):
    res_1 = calculate_wires(puzzle_input.copy())
    a = res_1['a']
    puzzle_input['b'] = [a]
    res_2 = calculate_wires(puzzle_input.copy())
    return res_2['a']


def calculate_wires(puzzle_input):
    res = {}
    while len(puzzle_input) > 0:
        if len(puzzle_input) == 1:
            print(puzzle_input)
        to_delete = []
        for key, value in puzzle_input.items():
            if len(value) == 1:
                try:
                    value = int(value[0])
                    res[key] = value
                    to_delete.append(key)
                    continue
                except ValueError:
                    pass
                if value[0] in res:
                    res[key] = res[value[0]]
                    to_delete.append(key)
            elif len(value) == 2 and value[1] in res:
                res[key] = ~ res[value[1]]
                to_delete.append(key)
            elif len(value) == 3:
                if value[1] == 'RSHIFT' and (value[0] in res or value[0] == '1'):
                    res[key] = (1 if value[0] == '1' else res[value[0]]) >> int(value[2])
                    to_delete.append(key)
                elif value[1] == 'LSHIFT' and (value[0] in res or value[0] == '1'):
                    res[key] = (1 if value[0] == '1' else res[value[0]]) << int(value[2])
                    to_delete.append(key)
                elif value[1] == 'AND' and (value[0] in res or value[0] == '1') and (
                        value[2] in res or value[2] == '1'):
                    res[key] = (1 if value[0] == '1' else res[value[0]]) & (1 if value[2] == '1' else res[value[2]])
                    to_delete.append(key)
                elif value[1] == 'OR' and (value[0] in res or value[0] == '1') and (value[2] in res or value[2] == '1'):
                    res[key] = (1 if value[0] == '1' else res[value[0]]) | (1 if value[2] == '1' else res[value[2]])
                    to_delete.append(key)
        for key in to_delete:
            puzzle_input.pop(key)
    return res


loaded_puzzle_input = helpers.load_puzzle_input(2015, 7)
parsed = [x.split(' -> ') for x in loaded_puzzle_input]
parsed = {x[1]: x[0].split(' ') for x in parsed}
print('Part one result: %s' % (helpers.run_and_time(part_one, parsed)))
print('Part two result: %s' % (helpers.run_and_time(part_two, parsed)))
