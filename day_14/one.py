import re


lines = [line.strip() for line in open("input").readlines()]
x_size = 101
y_size = 103
positions = []
velocities = []

for line in lines:
    x, y, vx, vy = map(int, re.findall(r"-*\d+", line))
    positions.append([x, y])
    velocities.append([vx, vy])

for _ in range(100):
    new_positions = []
    for (x, y), (vx, vy) in zip(positions, velocities):
        x_new = (x + vx) % x_size
        y_new = (y + vy) % y_size
        new_positions.append([x_new, y_new])
    positions = new_positions

robots_in_quadrant = [0] * 4
for x, y in positions:
    if x < x_size // 2 and y < y_size // 2:
        robots_in_quadrant[0] += 1
    elif x > x_size // 2 and y < y_size // 2:
        robots_in_quadrant[1] += 1
    elif x < x_size // 2 and y > y_size // 2:
        robots_in_quadrant[2] += 1
    elif x > x_size // 2 and y > y_size // 2:
        robots_in_quadrant[3] += 1
safety_factor = (
    robots_in_quadrant[0]
    * robots_in_quadrant[1]
    * robots_in_quadrant[2]
    * robots_in_quadrant[3]
)
print(safety_factor)
