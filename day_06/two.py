from common import parse_input, find_guard, rotated_guard_direction


lines = parse_input()
start_gi, start_gj, start_gdi, start_gdj = find_guard(lines)
possible_obstacles = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] != ".":
            continue
        oi, oj = i, j
        rotations = 0
        gi, gj, gdi, gdj = start_gi, start_gj, start_gdi, start_gdj
        unique_pos = set()
        unique_pos_len_from_last_full_rotation = 1
        while True:
            unique_pos.add((gi, gj))
            if rotations == 5:
                if len(unique_pos) == unique_pos_len_from_last_full_rotation:
                    possible_obstacles += 1
                    break
                else:
                    rotations = 0
                unique_pos_len_from_last_full_rotation = len(unique_pos)
            ngi, ngj = gi + gdi, gj + gdj
            if not (0 <= ngi < len(lines) and 0 <= ngj < len(lines[0])):
                break
            if lines[ngi][ngj] == "#" or (ngi, ngj) == (oi, oj):
                gdi, gdj = rotated_guard_direction(gdi, gdj)
                rotations += 1
            else:
                gi, gj = ngi, ngj
print(possible_obstacles)
