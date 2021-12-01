import requests
import time

def load_puzzle_input(day):
    url = 'https://adventofcode.com/2021/day/%d/input'%(day)
    cookies = dict(session='53616c7465645f5f3468d0ba844e5828d33dfe04f8640cd0655c59478f79e096c81cb660688e58a89f282b3109e67bc8')
    r = requests.get(url, cookies=cookies)

    r_list = list(r.text.split("\n"))
    r_list.pop()
    return r_list


def run_and_time(method, args):
    start_time = time.perf_counter_ns()
    result = method(args)
    end_time = time.perf_counter_ns()
    execution_time = (end_time - start_time) / 1000000
    return('%s, completed in %fms'%(result, execution_time))