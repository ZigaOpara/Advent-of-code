from operator import itemgetter

import helpers


def generate_file_system(puzzle_input):
    fs = {}
    path = []
    tmp_folder = {}
    for line in puzzle_input:
        if line.startswith('$ ls'):
            tmp_folder = {}
        elif line.startswith('$ cd'):
            if tmp_folder != {}:
                path_set(fs, path, tmp_folder)
            if line[5:] == '..':
                path.pop()
            else:
                path.append(line[5:])
            tmp_folder = {}
        elif line.startswith('dir'):
            tmp_folder[line[4:]] = {}
        else:
            file = line.split(' ')
            tmp_folder[file[1]] = int(file[0])
    path_set(fs, path, tmp_folder)
    return fs


def get_sizes_under_threshold(item, item_key='/', sizes_under_threshold=[], threshold=0):
    if type(item) is dict:
        size = 0
        for key in item.keys():
            s, sizes_under_threshold = get_sizes_under_threshold(item[key], key, sizes_under_threshold, threshold)
            size += s
        if threshold == 0 or size <= threshold:
            sizes_under_threshold.append((item_key, size))
        return size, sizes_under_threshold
    else:
        return item, sizes_under_threshold


def path_get(dictionary, path):
    for item in path:
        dictionary = dictionary[item]
    return dictionary


def path_set(dictionary, path, set_item):
    key = path[-1]
    dictionary = path_get(dictionary, path[:-1])
    dictionary[key] = set_item


def part_one(puzzle_input):
    _, sizes_under_threshold = get_sizes_under_threshold(item=puzzle_input, threshold=100000)
    return sum([x[1] for x in sizes_under_threshold])


def part_two(puzzle_input):
    total_size, sizes = get_sizes_under_threshold(item=puzzle_input)
    needed = 30000000 + total_size - 70000000
    return sorted([size for size in sizes if size[1] >= needed], key=itemgetter(1))[0][1]


loaded_puzzle_input = helpers.load_puzzle_input(2022, 7)
file_system = generate_file_system(loaded_puzzle_input)
print('Part one result: %s' % (helpers.run_and_time(part_one, file_system)))
print('Part two result: %s' % (helpers.run_and_time(part_two, file_system)))
