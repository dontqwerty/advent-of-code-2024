def is_collision(i, j):
    if grid[i][j] == "#":
        return True
    elif grid[i][j] == "@":
        to_move.append(((i, j), (di, dj)))
        return is_collision(i + di, j + dj)
    elif grid[i][j] == "O":
        to_move.append(((i, j), (di, dj)))
        return is_collision(i + di, j + dj)
    elif grid[i][j] == "]":
        to_move.append(((i, j), (di, dj)))
        return is_collision(i + di, j + dj)
    else:
        return False


grid, moves = open("input").read().split("\n\n")
grid = [list(g) for g in grid.splitlines()]
moves = "".join([m for m in moves.splitlines()])

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "@":
            ri, rj = i, j
            break

directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
for mix, move in enumerate(moves):
    di, dj = directions[move]
    to_move = []
    moved = []
    if is_collision(ri, rj):
        continue
    for ix, ((i, j), (di, dj)) in enumerate(reversed(to_move)):
        if (i, j) in moved:
            continue
        grid[i + di][j + dj] = grid[i][j]
        grid[i][j] = "."
        moved.append((i, j))
        if ix == len(to_move) - 1:
            ri, rj = i + di, j + dj

sum = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != "O":
            continue
        sum += 100 * i + j
print(sum)
