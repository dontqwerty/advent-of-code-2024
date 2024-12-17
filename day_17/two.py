import re
from z3 import Optimize, sat, BitVec

program = list(map(int, re.findall(r"\d+", open("input").read().split("\n\n")[1])))
a = BitVec("a", 64)
outs = [BitVec(f"out_{i}", 64) for i in range(len(program))]
o = Optimize()
o.add(a > 8 ** (len(program) - 1))
o.add(a < 8 ** (len(program)))
for i in range(len(program)):
    o.add(
        outs[i]
        == (
            ((((a >> (3 * i)) % 8) ^ 3) ^ 5)
            ^ ((a >> (3 * i)) >> (((a >> (3 * i)) % 8) ^ 3))
        )
        % 8
    )
    o.add(outs[i] == program[i])
o.minimize(a)
if o.check() == sat:
    result = int(o.model().evaluate(a).as_string())

print(result)
