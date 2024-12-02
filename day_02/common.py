import numpy as np


def parse_input():
    with open("input", "r") as f:
        return [list(map(int, line.split())) for line in f.readlines()]


def check_report(line):
    diffs = np.array([line[k + 1] - line[k] for k in range(len(line) - 1)])
    return (np.logical_and(diffs > 0, diffs < 4)).all() or (
        np.logical_and(diffs < 0, diffs > -4).all()
    )
