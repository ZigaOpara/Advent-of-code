import helpers
import numpy

def flash(input, x, y, flashed):
    if x < 0 or y < 0 or flashed[x, y]:
        return
    flashed[x, y] = True
    neighbours = [
        [x-1, y-1], [x-1, y], [x-1, y+1],
        [x, y-1], [x, y+1],
        [x+1, y-1], [x+1, y], [x+1, y+1],
    ]
    for neighbour in neighbours:
        if neighbour[0] < 0 or neighbour[1] < 0 or neighbour[0] >= len(input) or neighbour[1] >= len(input):
            continue
        try:
            input[neighbour[0]][neighbour[1]] += 1
            if input[neighbour[0]][neighbour[1]] > 9 and flashed[neighbour[0]][neighbour[1]] == False:
                flash(input, neighbour[0], neighbour[1], flashed)
        except:
            continue


def part_one(input):
    flashes = 0
    for _ in range(100):
        flashed = numpy.full((len(input), len(input[0])), False)
        for x, line in enumerate(input):
            for y, octopus in enumerate(line):
                input[x][y] += 1
                if input[x][y] > 9:
                    flash(input, x, y, flashed)
        input = [[0 if x > 9 else x for x in y] for y in input]
        flashes += sum(x.count(0) for x in input)
    return flashes


def part_two(input):
    for n in range(1000):
        flashed = numpy.full((len(input), len(input[0])), False)
        for x, line in enumerate(input):
            for y, octopus in enumerate(line):
                input[x][y] += 1
                if input[x][y] > 9:
                    flash(input, x, y, flashed)
        input = [[0 if x > 9 else x for x in y] for y in input]
        if numpy.all(numpy.array(input) == 0):
            return n+1
    return


input = helpers.load_puzzle_input(11)
input = list(map(lambda x: list(map(int, list(x))), input))
test_input = [
    [5,4,8,3,1,4,3,2,2,3],
    [2,7,4,5,8,5,4,7,1,1],
    [5,2,6,4,5,5,6,1,7,3],
    [6,1,4,1,3,3,6,1,4,6],
    [6,3,5,7,3,8,5,4,7,8],
    [4,1,6,7,5,2,4,6,4,5],
    [2,1,7,6,8,4,1,7,2,1],
    [6,8,8,2,8,8,1,1,3,4],
    [4,8,4,6,8,4,8,5,5,4],
    [5,2,8,3,7,5,1,5,2,6],
]
test_input_2 = [
    [1,1,1,1,1],
    [1,9,9,9,1],
    [1,9,1,9,1],
    [1,9,9,9,1],
    [1,1,1,1,1],
]
print('Part one result: %s' % (helpers.run_and_time(part_one, input)))
print('Part two result: %s' % (helpers.run_and_time(part_two, input)))