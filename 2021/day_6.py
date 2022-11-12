import helpers


def get_n_of_fish_in_days(input, days):
    fish_dict = {
        0: input.count(0),
        1: input.count(1),
        2: input.count(2),
        3: input.count(3),
        4: input.count(4),
        5: input.count(5),
        6: input.count(6),
        7: input.count(7),
        8: input.count(8),
    }
    for day in range(days):
        tmp = dict(fish_dict)
        new_fish = 0
        for key in tmp:
            if key == 0:
                new_fish = tmp[0]
                continue
            fish_dict[key - 1] = fish_dict[key]
        fish_dict[8] = new_fish
        fish_dict[6] += new_fish
    
    result = 0
    for key in fish_dict:
        result += fish_dict[key]
    return result
    


def part_one(input):
    return get_n_of_fish_in_days(input, 80)


def part_two(input):
    return get_n_of_fish_in_days(input, 256)


input = helpers.load_puzzle_input(6)
input = list(map(int, list(input[0].split(","))))
print('Part one result: %s' % (helpers.run_and_time(part_one, input)))
print('Part two result: %s' % (helpers.run_and_time(part_two, input)))