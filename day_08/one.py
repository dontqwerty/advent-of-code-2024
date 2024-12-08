from common import parse_input, get_antennas

lines = parse_input()
antennas = get_antennas(lines)
antinodes = set()
for antenna_coords in antennas.values():
    for coord_0 in antenna_coords:
        for coord_1 in antenna_coords:
            if coord_0 == coord_1:
                continue
            dx = coord_0[0] - coord_1[0]
            dy = coord_0[1] - coord_1[1]
            antinode = (coord_0[0] + dx, coord_0[1] + dy)
            if 0 <= antinode[0] < len(lines) and 0 <= antinode[1] < len(lines[0]):
                antinodes.add(antinode)
print(len(antinodes))
