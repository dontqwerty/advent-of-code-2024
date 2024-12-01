from common import parse_input

left, right = parse_input()
sum = 0
for i in left:
    sum += i * right.count(i)
print(sum)
