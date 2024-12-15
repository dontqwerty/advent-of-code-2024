from typing import List


def is_collision(i, j):
    if grid[i][j] == "#":
        return True
    elif grid[i][j] == "@":
        to_move.append(((i, j), (di, dj)))
        return is_collision(i + di, j + dj)
    elif grid[i][j] == "[":
        to_move.append(((i, j), (di, dj)))
        c1 = is_collision(i + di, j + dj)
        c2 = False
        if di != 0:
            to_move.append(((i, j + 1), (di, dj)))
            c2 = is_collision(i + di, j + 1 + dj)
        return c1 or c2
    elif grid[i][j] == "]":
        to_move.append(((i, j), (di, dj)))
        c1 = is_collision(i + di, j + dj)
        c2 = False
        if di != 0:
            to_move.append(((i, j - 1), (di, dj)))
            c2 = is_collision(i + di, j - 1 + dj)
        return c1 or c2
    else:
        return False


grid, moves = open("input").read().split("\n\n")
grid = [list(g) for g in grid.splitlines()]
moves = "".join([m for m in moves.splitlines()])

new_grid: List[List[str]] = []
replacements = {"#": list("##"), ".": list(".."), "O": list("[]"), "@": list("@.")}
for i in range(len(grid)):
    new_grid.append([])
    for j in range(len(grid[0])):
        new_grid[i].extend(replacements[grid[i][j]])
grid = new_grid

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
        if grid[i][j] != "[":
            continue
        sum += 100 * i + j
print(sum)
