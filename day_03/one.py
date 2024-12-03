import re

from common import parse_input

matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", parse_input())
sum = 0
for match in matches:
    numbers = list(map(int, re.findall(r"\d{1,3}", match)))
    sum += numbers[0] * numbers[1]
print(sum)
