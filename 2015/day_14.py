import helpers


def part_one(puzzle_input):
    max_traveled = 0
    for raindeer in puzzle_input.values():
        full_cycles, rest = divmod(2503, (raindeer[1] + raindeer[2]))
        traveled = ((full_cycles * raindeer[1]) + min(rest, raindeer[1])) * raindeer[0]
        max_traveled = max(traveled, max_traveled)
    return max_traveled


def part_two(puzzle_input):
    distance = {}
    points = {}
    for i in range(2503):
        for name, raindeer in puzzle_input.items():
            moving = i % (raindeer[1] + raindeer[2]) < raindeer[1]
            if moving:
                if name in distance.keys():
                    distance[name] += raindeer[0]
                else:
                    distance[name] = raindeer[0]
        furthest_distance = sorted(distance.values())[-1]
        leaders = [key for (key, value) in distance.items() if value == furthest_distance]
        for leader in leaders:
            if leader in points.keys():
                points[leader] += 1
            else:
                points[leader] = 1
    return sorted(points.values())[-1]


loaded_puzzle_input = helpers.load_puzzle_input(2015, 14)
parsed = {x[0]: (int(x[3]), int(x[6]), int(x[13])) for x in (y.split(' ') for y in loaded_puzzle_input)}
print('Part one result: %s' % (helpers.run_and_time(part_one, parsed)))
print('Part two result: %s' % (helpers.run_and_time(part_two, parsed)))
