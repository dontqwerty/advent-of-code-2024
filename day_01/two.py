from common import parse_input

left, right = parse_input()
sum = 0
for i in left:
    i_in_right = 0
    for k in right:
        if i == k:
            i_in_right += 1
    sum += i * i_in_right
print(sum)
