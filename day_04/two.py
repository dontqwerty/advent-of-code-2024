from common import parse_input

lines = parse_input()
count = 0
for i in range(1, len(lines) - 1):
    for j in range(1, len(lines[0]) - 1):
        if (
            lines[i][j] != "A"
            or set([lines[i - 1][j - 1], lines[i + 1][j + 1]]) != set(["M", "S"])
            or set([lines[i - 1][j + 1], lines[i + 1][j - 1]]) != set(["M", "S"])
        ):
            continue
        count += 1
print(count)
