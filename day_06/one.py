from common import parse_input, find_guard, rotated_guard_direction


lines = parse_input()
gi, gj, gdi, gdj = find_guard(lines)
unique_pos = set()
while True:
    unique_pos.add((gi, gj))
    ngi, ngj = gi + gdi, gj + gdj
    if not (0 <= ngi < len(lines) and 0 <= ngj < len(lines[0])):
        break
    if lines[ngi][ngj] == "#":
        gdi, gdj = rotated_guard_direction(gdi, gdj)
    else:
        gi, gj = ngi, ngj
print(len(unique_pos))
