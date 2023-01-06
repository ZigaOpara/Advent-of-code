import os
import time
import typing
import operator

import numpy as np
import requests


def load_puzzle_raw(year: int, day: int) -> requests.Response:
    url = 'https://adventofcode.com/{year}/day/{day}/input'.format(year=year, day=day)
    cookies = dict(
        session='53616c7465645f5f79932d8557876ba0215a35ed4a897a7646fee7f40a4d98f1e58e3f331122374b4d2242ed502a8ada00932ccda04ed34e71c268688d2730d3')
    r = requests.get(url, cookies=cookies)
    return r


def load_puzzle_input(year: int, day: int) -> list:
    r = load_puzzle_raw(year, day)
    r_list = list(r.text.split("\n"))
    r_list.pop()
    return r_list


def load_test_puzzle_input() -> list:
    with open(os.path.join(os.path.dirname(__file__), 'test.txt')) as f:
        return f.read().splitlines()


def run_and_time(method: typing.Callable, *args) -> str:
    start_time = time.perf_counter_ns()
    result = method(*args)
    end_time = time.perf_counter_ns()
    execution_time = (end_time - start_time) / 1000000
    return '%s, completed in %fms' % (result, execution_time)


def get_neighbours(grid: typing.Union[list, np.array], node: tuple, diagonals: bool = False) -> list[tuple]:
    sides = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    if diagonals:
        sides.extend([[-1, -1], [-1, 1], [1, 1], [1, -1]])
    neighbours = [(node[0] + x, node[1] + y) for x, y in [[-1, 0], [0, -1], [1, 0], [0, 1]]]
    for neighbour in neighbours.copy():
        try:
            if neighbour[0] < 0 or neighbour[1] < 0:
                raise IndexError
            n = operator.itemgetter(neighbour)(grid) if isinstance(grid, list) else grid[neighbour]
        except IndexError:
            neighbours.remove(neighbour)
            continue
    return neighbours
