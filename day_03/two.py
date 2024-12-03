import re

from common import parse_input

matches = re.findall(r"do\(\)|mul\(\d{1,3},\d{1,3}\)|don't\(\)", parse_input())
sum = 0
do_sum = True
for match in matches:
    if re.match(r"do\(\)", match):
        do_sum = True
    elif re.match(r"don't\(\)", match):
        do_sum = False
    elif do_sum:
        numbers = list(map(int, re.findall(r"\d{1,3}", match)))
        sum += numbers[0] * numbers[1]
print(sum)
