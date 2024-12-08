from typing import Dict, List, Tuple


def parse_input() -> List[str]:
    return [line.strip() for line in open("input").readlines()]


def get_antennas(lines: List[str]) -> Dict[str, List[Tuple[int, int]]]:
    antennas: Dict[str, List[Tuple[int, int]]] = {}
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] != ".":
                if lines[i][j] not in antennas:
                    antennas[lines[i][j]] = [(i, j)]
                else:
                    antennas[lines[i][j]].append((i, j))
    return antennas
