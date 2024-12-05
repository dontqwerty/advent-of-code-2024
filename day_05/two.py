from common import parse_input, get_update_indices, find_sorted_updates

rules, updates = parse_input()
sorted_updates = find_sorted_updates(rules, updates)
manually_sorted_updates = []
sum = 0
for update in updates:
    if update in sorted_updates:
        continue
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        update_ixs = get_update_indices(update)
        for first, last in rules:
            try:
                if not update_ixs[first] < update_ixs[last]:
                    first_ix, last_ix = update.index(first), update.index(last)
                    update[first_ix], update[last_ix] = (
                        update[last_ix],
                        update[first_ix],
                    )
                    is_sorted = False
                    break
            except (KeyError, ValueError):
                pass
    manually_sorted_updates.append(update)

sum = 0
for update in manually_sorted_updates:
    sum += update[len(update) // 2]
print(sum)
