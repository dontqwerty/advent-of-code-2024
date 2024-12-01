from typing import Tuple, List


def parse_input() -> Tuple[List[int], List[int]]:
    with open("input", "r") as f:
        lists = [list(map(int, line.split())) for line in f]
    return tuple(map(list, zip(*lists)))
