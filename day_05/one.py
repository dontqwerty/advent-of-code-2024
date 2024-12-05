from common import parse_input, find_sorted_updates

rules, updates = parse_input()
sum = 0
for update in find_sorted_updates(rules, updates):
    sum += update[len(update) // 2]
print(sum)
