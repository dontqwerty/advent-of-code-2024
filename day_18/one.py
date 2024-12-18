import re
import heapq

x_size, y_size = 71, 71
walls = set(
    [
        tuple(map(int, re.findall(r"\d+", line)))
        for line in open("input").read().splitlines()
    ][:1024]
)
q = []
visited = set()
seen = dict()
heapq.heappush(q, (0, 0, 0))
while q:
    steps, x, y = heapq.heappop(q)
    if (x, y) == (x_size - 1, y_size - 1):
        print(steps)
        break
    visited.add((x, y))
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if (
            not (0 <= nx < x_size and 0 <= ny < y_size)
            or (nx, ny) in walls
            or (nx, ny) in visited
        ):
            continue
        nsteps = steps + 1
        if (nx, ny) not in seen or seen[(nx, ny)] > nsteps:
            heapq.heappush(q, (nsteps, nx, ny))
            seen[(nx, ny)] = nsteps
