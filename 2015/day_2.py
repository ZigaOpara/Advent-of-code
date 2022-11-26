import helpers


def part_one(puzzle_input):
    sqr_ft_of_paper = 0
    for box in puzzle_input:
        sqr_ft_of_paper += 3 * box[0] * box[1] + 2 * box[1] * box[2] + 2 * box[2] * box[0]
    return sqr_ft_of_paper


def part_two(puzzle_input):
    ft_of_ribbon = 0
    for box in puzzle_input:
        ft_of_ribbon += 2 * box[0] + 2 * box[1] + box[0] * box[1] * box[2]
    return ft_of_ribbon


loaded_puzzle_input = helpers.load_puzzle_input(2015, 2)
parsed = [sorted([int(x) for x in y.split('x')]) for y in loaded_puzzle_input]
print('Part one result: %s' % (helpers.run_and_time(part_one, parsed)))
print('Part two result: %s' % (helpers.run_and_time(part_two, parsed)))
