from typing import Tuple, List


def parse_input() -> Tuple[List[int], List[int]]:
    with open("input", "r") as f:
        lists = [[int(k) for k in i.split("   ")] for i in f.readlines()]
    return map(list, zip(*lists))
