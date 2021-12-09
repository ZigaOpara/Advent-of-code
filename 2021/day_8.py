import helpers


def part_one(input):
    result = 0
    for line in input:
        result += len([elem for elem in line[1] if len(elem) in (2, 3, 4, 7)])
    return result


def part_two(input):
    for line in input:
        
    return



input = helpers.load_puzzle_input(8)
input = list(map(lambda x: x.split(" | "), input))
input = list(map(lambda x: list(map(lambda y: y.split(" "), x)), input))
print('Part one result: %s'%(helpers.run_and_time(part_one, input)))
# print('Part two result: %s'%(helpers.run_and_time(part_two, input)))