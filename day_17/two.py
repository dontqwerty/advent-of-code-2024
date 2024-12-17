"""
### Day 17 - Part 2: Chronospatial Computer

This solution is based on the input and thus it is only valid for this specific input.

#### Program pseudocode

The following pseudocode describes the operations in the input and their effects.

```
bst A   # B ← A mod 8
blx 3   # B ← B xor 3
cdv B   # C ← A >> B
bxl 5   # B ← B xor 5
adv 3   # A ← A >> 3
bxc 3   # B ← B xor C
out B   # print B mod 8
jnz 0   # if A != 0: IP ← 0
```

#### Analysis

Looking at the program starting from the last line, it appears that:

- The program will only halt if ``A`` is ``0``. In every other case it will start
again from the first instruction.
- During the entire execution, only ``B`` is printed out and this happens exactly once for every
iteration of the program.
- ``A`` gets divided by ``8`` at the end of every iteration.
- For the initial value of ``A`` to be correct, it must be greater that ``8^15`` and less than
``8^16`` in order to become ``0`` at the end of the 16th iteration: after 16 printed values of ``B``.

Expanding how ``B`` is computed, starting from the end of the program, gives:

```
B ← B mod 8
B ← (B xor C) mod 8
B ← ((B xor 5) xor (A >> B)) mod 8
B ← (((B xor 3) xor 5) xor (A >> (B xor 3))) mod 8
B ← ((((A mod 8) xor 3) xor 5) xor (A >> ((A mod 8) xor 3))) mod 8
```

Notably, there is a direct mapping from ``A`` to ``B`` on every iteration. This means that on every
iteration ``B`` is computed based only on the value of ``A`` at the beginning of the iteration.

The minimum value of ``A`` that correctly computes ``B`` is found using the ``z3-solver`` library.

Specifically, ``18`` constrains and ``1`` objective are added optimizer model of the ``z3`` module:

- 2 constrains to fix an upper and lower bound of ``A``. This is not necessary for the
solution to work, but it makes the execution time slighlty faster.
- 16 constrains to make sure that the expanded form of ``B`` in the ``nth`` iteration is
equal to the ``nth`` element in the input program as ``A`` is repeatedly divided by ``8``.
- 1 objective to make sure that ``A`` is as small as possible.
"""

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
