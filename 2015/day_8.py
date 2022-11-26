import ast
import helpers


def part_one(puzzle_input):
    code = 0
    memory = 0
    for string in puzzle_input:
        code += len(string)
        memory += len(ast.literal_eval(string))
    return code - memory


def part_two(puzzle_input):
    old = 0
    new = 0
    for string in puzzle_input:
        new_str = '"{0}"'.format(string.replace('\\', '\\\\').replace('"', '\\"'))
        old += len(string)
        new += len(new_str)
    return new - old


loaded_puzzle_input = helpers.load_puzzle_input(2015, 8)
print('Part one result: %s' % (helpers.run_and_time(part_one, loaded_puzzle_input)))
print('Part two result: %s' % (helpers.run_and_time(part_two, loaded_puzzle_input)))
