def get_inline(ii, ij, di, dj):
    inline = [(ii, ij, di, dj)]
    if dj == 0:
        for j in range(ij + 1, len(lines[0])):
            if 0 <= ii - di and lines[ii - di][j] != current_plant:
                break
            inline.append((ii, j, di, dj))
        for j in reversed(range(0, ij)):
            if (0 <= ii < len(lines) and lines[ii][j] == current_plant) or (
                0 <= ii - di < len(lines) and lines[ii - di][j] != current_plant
            ):
                break
            inline.append((ii, j, di, dj))
    else:
        for i in range(ii + 1, len(lines)):
            if 0 <= ij - dj < len(lines[0]) and lines[i][ij - dj] != current_plant:
                break
            inline.append((i, ij, di, dj))
        for i in reversed(range(0, ii)):
            if (0 <= ij < len(lines[0]) and lines[i][ij] == current_plant) or (
                0 <= ij - dj < len(lines[0]) and lines[i][ij - dj] != current_plant
            ):
                break
            inline.append((i, ij, di, dj))
    return inline


def perimeter_is_inline(i, j, di, dj):
    for inline in get_inline(i, j, di, dj):
        if inline in checked_perimeters:
            return True
    return False


def get_perimeter(ii, ij):
    p = 0
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        i, j = ii + di, ij + dj
        if (
            0 <= i < len(lines)
            and 0 <= j < len(lines[0])
            and not lines[i][j] != current_plant
        ):
            continue
        if not perimeter_is_inline(i, j, di, dj):
            checked_perimeters.append((i, j, di, dj))
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
        checked_perimeters = []
        set_checked_positions(i, j)
        p = 0
        for pi, pj in sorted(checked_positions):
            current_plant = lines[pi][pj]
            pp = get_perimeter(pi, pj)
            p += pp
        cost += len(checked_positions) * p
        all_checked_positions.extend(checked_positions)
print(cost)
