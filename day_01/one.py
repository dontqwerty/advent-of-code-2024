from common import parse_input

left, right = parse_input()
left.sort()
right.sort()
sum = 0
for i, k in zip(left, right):
    sum += abs(i - k)
print(sum)
