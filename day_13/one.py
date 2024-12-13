import re

total_cost = 0
for claw in open("input").read().split("\n\n"):
    a_x, a_y, b_x, b_y, target_x, target_y = map(int, re.findall(r"\d+", claw))
    min_cost = None
    for a_coeff in range(101):
        for b_coeff in range(101):
            if (
                a_x * a_coeff + b_x * b_coeff == target_x
                and a_y * a_coeff + b_y * b_coeff == target_y
            ):
                cost = a_coeff * 3 + b_coeff
                if min_cost is None or min_cost > cost:
                    min_cost = cost
    if min_cost is not None:
        total_cost += min_cost

print(total_cost)
