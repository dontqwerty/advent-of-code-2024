from typing import List


def parse_input() -> str:
    return [line.strip() for line in open("input").readlines()]


def find_guard(lines: List[str]):
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "^":
                return i, j, -1, 0
            elif lines[i][j] == "v":
                return i, j, 1, 0
            elif lines[i][j] == ">":
                return i, j, 0, 1
            elif lines[i][j] == "<":
                return i, j, 0, -1


def rotated_guard_direction(gdi: int, gdj: int):
    if gdi == -1:
        return 0, 1
    elif gdi == 1:
        return 0, -1
    elif gdj == -1:
        return -1, 0
    elif gdj == 1:
        return 1, 0
