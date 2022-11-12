import helpers
import numpy

def find_low_points(input):
    low_points = []
    for x in range(len(input)):
        for y in range(len(input[0])):
            selected_element = input[x][y]
            is_smallest = True
            for neighbour in [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]:
                try:
                    if input[neighbour[0]][neighbour[1]] <= selected_element:
                        is_smallest = False
                        break
                except:
                    continue
            if is_smallest:
                low_points.append([selected_element, x, y])
    return low_points


def count_basin(input, x, y, seen=[]):
    seen.append([x, y])
    selected_element = input[x][y]
    temp_res = 1
    for neighbour in [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]:
        if neighbour in seen or neighbour[0] < 0 or neighbour[1] < 0:
            continue
        try:
            if input[neighbour[0]][neighbour[1]] >= selected_element and input[neighbour[0]][neighbour[1]] < 9:
                temp_res += count_basin(input, neighbour[0], neighbour[1], seen)
        except:
            continue
    return temp_res


def part_one(input):
    low_points = list(map(lambda x: x[0], find_low_points(input)))
    risk_level_sum = sum(map(lambda x: x+1, low_points))
    return risk_level_sum


def part_two(input):
    low_points = list(map(lambda x: [x[1], x[2]], find_low_points(input)))
    basins = []
    for low_point in low_points:
        basins.append(count_basin(input, low_point[0], low_point[1]))
    top_three = sorted(basins, reverse=True)[:3]
    return numpy.prod(top_three)


input = helpers.load_puzzle_input(9)
input = list(map(lambda x: list(map(int, [*x])), input))
print('Part one result: %s' % (helpers.run_and_time(part_one, input)))
print('Part two result: %s' % (helpers.run_and_time(part_two, input)))