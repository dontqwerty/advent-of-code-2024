def get_perimeter(ii, ij):
    p = 0
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        i, j = ii + di, ij + dj
        if (
            not (0 <= i < len(lines) and 0 <= j < len(lines[0]))
            or lines[i][j] != lines[ii][ij]
        ):
            p += 1
    return p


def set_checked_positions(ii, ij):
    checked_positions.append((ii, ij))
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        i, j = ii + di, ij + dj
        if (i, j) in checked_positions:
            continue
        if not (0 <= i < len(lines) and 0 <= j < len(lines[0])):
            continue
        if lines[i][j] == lines[ii][ij]:
            set_checked_positions(i, j)


lines = [line.strip() for line in open("input").readlines()]
all_checked_positions = []
cost = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if (i, j) in all_checked_positions:
            continue
        checked_positions = []
        set_checked_positions(i, j)
        p = 0
        for plant_position in checked_positions:
            p += get_perimeter(plant_position[0], plant_position[1])
        cost += len(checked_positions) * p
        all_checked_positions.extend(checked_positions)
print(cost)
