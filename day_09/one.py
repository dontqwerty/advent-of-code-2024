from common import parse_input


def check(s):
    first_free = 0
    for ix, c in enumerate(s):
        if c != ".":
            continue
        first_free = ix
        break
    for i in range(first_free, len(s)):
        if s[i] != ".":
            return False
    return True


line = parse_input()
s = []
id = 0
for ix, c in enumerate(line):
    if ix % 2 == 0:
        for n in range(int(c)):
            s.append(str(id))
        id += 1
    else:
        for n in range(int(c)):
            s.append(".")

free = []
for ix, c in enumerate(s):
    if c == ".":
        free.append(ix)

free_ix = 0
s_rev = s[::-1]
for ix, c in enumerate(s_rev):
    if check(s):
        break
    if c == ".":
        continue
    s[free[free_ix]] = c
    s[len(s) - (ix + 1)] = "."
    free_ix += 1

checksum = 0
id = 0
current = None
increase_id = False
for ix, c in enumerate(s):
    if c == ".":
        break
    if current is None or current != int(c):
        current = int(c)
        increase_id = True
    checksum += id * current
    if increase_id:
        id += 1
print(checksum)
