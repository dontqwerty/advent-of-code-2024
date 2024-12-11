line = list(map(int, open("input").readline().strip().split()))

size = len(line)
for i in range(25):
    new_line = []
    for n in line:
        if n == 0:
            new_line.append(1)
        elif len(str(n)) % 2 == 0:
            n_str = str(n)
            new_line.append(int(n_str[: len(n_str) // 2]))
            new_line.append(int(n_str[len(n_str) // 2 :]))
            size += 1
        else:
            new_line.append(n * 2024)
    line = new_line

print(size)
