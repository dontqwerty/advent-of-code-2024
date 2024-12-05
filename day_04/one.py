from common import parse_input

WORD = "XMAS"
DIRECTIONS = [
    lambda i, j: (i - 1, j),
    lambda i, j: (i + 1, j),
    lambda i, j: (i, j - 1),
    lambda i, j: (i, j + 1),
    lambda i, j: (i - 1, j - 1),
    lambda i, j: (i - 1, j + 1),
    lambda i, j: (i + 1, j - 1),
    lambda i, j: (i + 1, j + 1),
]

lines = parse_input()
count = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] != WORD[0]:
            continue
        for direction in DIRECTIONS:
            found = True
            ii, jj = i, j
            for word_ix in range(1, len(WORD)):
                ii, jj = direction(ii, jj)
                if (
                    ii < 0
                    or jj < 0
                    or ii >= len(lines)
                    or jj >= len(lines[0])
                    or lines[ii][jj] != WORD[word_ix]
                ):
                    found = False
                    break
            count += int(found)
print(count)
