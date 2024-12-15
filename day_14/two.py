import re
from collections import Counter


def print_grid(positions_count: Counter):
    for y in range(y_size):
        line = ""
        for x in range(x_size):
            if (x, y) in positions_count.keys():
                line += f"{positions_count[(x, y)]}"
            else:
                line += "."
        print(line)


lines = [line.strip() for line in open("input").readlines()]
x_size = 101
y_size = 103
positions = []
velocities = []

for line in lines:
    x, y, vx, vy = map(int, re.findall(r"-*\d+", line))
    positions.append([x, y])
    velocities.append([vx, vy])

i = 0
while True:
    i += 1
    new_positions = []
    for (x, y), (vx, vy) in zip(positions, velocities):
        x_new = (x + vx) % x_size
        y_new = (y + vy) % y_size
        new_positions.append((x_new, y_new))
    positions = new_positions

    max_x_positions_count = Counter([p[0] for p in positions]).most_common(1)[0][1]
    max_y_positions_count = Counter([p[1] for p in positions]).most_common(1)[0][1]
    if max_x_positions_count > y_size // 5 and max_y_positions_count > x_size // 5:
        print_grid(Counter(positions))
        if input(f"Current iteration: {i}. Is there a christmas tree? [y/N]: ") == "y":
            break
