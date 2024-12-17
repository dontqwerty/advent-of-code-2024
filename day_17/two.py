import re
from z3 import Optimize, sat, BitVec

prog = list(map(int, re.findall(r"\d+", open("input").read().split("\n\n")[1])))
a = BitVec("A", 64)
o = Optimize()
o.add(a > 8 ** (len(prog) - 1))
o.add(a < 8 ** (len(prog)))
for i in range(len(prog)):
    o.add(
        (
            ((((a >> (3 * i)) % 8) ^ 3) ^ 5)
            ^ ((a >> (3 * i)) >> (((a >> (3 * i)) % 8) ^ 3))
        )
        % 8
        == prog[i]
    )
o.minimize(a)
assert o.check() == sat
print(o.model().evaluate(a))
