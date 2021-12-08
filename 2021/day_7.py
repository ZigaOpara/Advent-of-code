import helpers
import statistics
import sys


def part_one(input):
    median = statistics.median(input)
    result = 0
    for position in input:
        result += abs(position - median)
    return int(result)


def part_two(input):
    best_res = sys.maxsize
    average = int(round(sum(input) / len(input)))
    for i in range(100):
        result = 0
        for position in input:
            distance = abs(position - average + i)
            result += sum(range(1, distance + 1))
        if result < best_res:
            best_res = result
        result = 0
        for position in input:
            distance = abs(position - average - i)
            result += sum(range(1, distance + 1))
        if result < best_res:
            best_res = result
    return best_res



input = helpers.load_puzzle_input(7)
input = list(map(int, list(input[0].split(","))))
print('Part one result: %s'%(helpers.run_and_time(part_one, input)))
print('Part two result: %s'%(helpers.run_and_time(part_two, input)))