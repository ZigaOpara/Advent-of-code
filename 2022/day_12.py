import numpy as np

import helpers


def part_one(grid, start, end):
    explored = []
    queue = [[start]]

    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = helpers.get_neighbours(grid, node)
            value = grid[node]

            for neighbour in neighbours:
                if grid[neighbour] - value > 1:
                    continue
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == end:
                    return len(new_path) - 1

            explored.append(node)


def part_two(grid, start):
    explored = []
    queue = [[start]]

    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = helpers.get_neighbours(grid, node)
            value = grid[node]

            for neighbour in neighbours:
                if value - grid[neighbour] > 1:
                    continue
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if grid[neighbour] == ord('a'):
                    return len(new_path) - 1

            explored.append(node)


loaded_puzzle_input = helpers.load_puzzle_input(2022, 12)
parsed = np.array(list(map(lambda x: list(x), loaded_puzzle_input)))
s = list(zip(*np.where(parsed == 'S')))[0]
e = list(zip(*np.where(parsed == 'E')))[0]
parsed = np.vectorize(lambda x: ord(x))(parsed)
parsed[parsed == ord('E')] = ord('z')
parsed[parsed == ord('S')] = ord('a')
print('Part one result: %s' % (helpers.run_and_time(part_one, parsed, s, e)))
print('Part two result: %s' % (helpers.run_and_time(part_two, parsed, e)))
