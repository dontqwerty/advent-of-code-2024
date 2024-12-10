from common import parse_input

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


ids = set(s)
ids_count = {}
for id in ids:
    ids_count[id] = s.count(id)


while True:
    change_done = False
    s_rev = s[::-1]
    checked_ids = set()
    for ix, c in enumerate(s_rev):
        if c == "." or c in checked_ids:
            continue
        checked_ids.add(c)
        free_start = -1
        for cix, cc in enumerate(s):
            try:
                if s[cix : cix + ids_count[c]] == ["."] * ids_count[c]:
                    free_start = cix
                    break
            except IndexError:
                break
        if free_start == -1:
            continue

        free_end = free_start + ids_count[c]
        to_free_start = len(s) - ix - ids_count[c]
        to_free_end = to_free_start + ids_count[c]
        if free_start > to_free_start:
            continue
        change_done = True
        s[free_start:free_end] = [c] * ids_count[c]
        s[to_free_start:to_free_end] = ["."] * ids_count[c]

    if not change_done:
        break
    break

checksum = 0
for ix, c in enumerate(s):
    if c == ".":
        continue
    checksum += int(c) * ix
print(checksum)
