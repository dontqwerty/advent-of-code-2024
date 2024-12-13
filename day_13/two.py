import re
from z3 import Optimize, Int, sat

total_cost = 0
for claw in open("input").read().split("\n\n"):
    a_x, a_y, b_x, b_y, target_x, target_y = map(int, re.findall(r"\d+", claw))
    a_coeff = Int("a_coeff")
    b_coeff = Int("b_coeff")
    cost = a_coeff * 3 + b_coeff
    o = Optimize()
    o.add(a_x * a_coeff + b_x * b_coeff == target_x + 10000000000000)
    o.add(a_y * a_coeff + b_y * b_coeff == target_y + 10000000000000)
    o.minimize(cost)
    if o.check() == sat:
        total_cost += int(o.model().evaluate(cost).as_string())

print(total_cost)
