import time
import typing

import requests


def load_puzzle_raw(year: int, day: int) -> requests.Response:
    url = 'https://adventofcode.com/{year}/day/{day}/input'.format(year=year, day=day)
    cookies = dict(
        session='53616c7465645f5f987485fe3408d6f940e3a545eebd738cde54c938c6c835e04fa37a98b23edb96e6fffd4d86e25d51415eaf0ad75387a56debc77966ebc973')
    r = requests.get(url, cookies=cookies)
    return r


def load_puzzle_input(year: int, day: int) -> list:
    r = load_puzzle_raw(year, day)
    r_list = list(r.text.split("\n"))
    r_list.pop()
    return r_list


def run_and_time(method: typing.Callable, *args) -> str:
    start_time = time.perf_counter_ns()
    result = method(*args)
    end_time = time.perf_counter_ns()
    execution_time = (end_time - start_time) / 1000000
    return '%s, completed in %fms' % (result, execution_time)
