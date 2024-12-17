import re

reg, prog = open("input").read().split("\n\n")
reg = {r: v for r, v in zip(["A", "B", "C"], map(int, re.findall(r"\d+", reg)))}
reg["PC"] = 0
prog = list(map(int, re.findall(r"\d+", prog)))
out = []

coms = {
    0: lambda: 0,
    1: lambda: 1,
    2: lambda: 2,
    3: lambda: 3,
    4: lambda: reg["A"],
    5: lambda: reg["B"],
    6: lambda: reg["C"],
}

ops = {
    0: ("A", lambda com: reg["A"] >> coms[com]()),
    1: ("B", lambda lit: reg["B"] ^ lit),
    2: ("B", lambda com: coms[com]() % 8),
    3: ("PC", lambda lit: reg["PC"] if reg["A"] == 0 else lit - 2),
    4: ("B", lambda _: reg["B"] ^ reg["C"]),
    5: (None, lambda com: out.append(coms[com]() % 8)),
    6: ("B", lambda com: reg["A"] >> coms[com]()),
    7: ("C", lambda com: reg["A"] >> coms[com]()),
}

while 0 <= reg["PC"] <= len(prog) - 2:
    operation, operand = (
        prog[reg["PC"]],
        prog[reg["PC"] + 1],
    )
    dest = ops[operation][0]
    result = ops[operation][1](operand)
    if dest is not None:
        reg[dest] = ops[operation][1](operand)
    reg["PC"] += 2
print(",".join(map(str, out)))
