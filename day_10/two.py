from common import parse_input

lines = parse_input()


def hike(ii, ij):
    if lines[ii][ij] == 9 and (ii, ij):
        return 1
    score = 0
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        i, j = ii + di, ij + dj
        if (
            not (0 <= i < len(lines) and 0 <= j < len(lines[0]))
            or lines[i][j] - lines[ii][ij] != 1
        ):
            continue
        score += hike(i, j)
    return score


score = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] != 0:
            continue
        score += hike(i, j)
print(score)
