import re

registers, program = open("input").read().split("\n\n")
registers = {
    r: v for r, v in zip(["A", "B", "C"], map(int, re.findall(r"\d+", registers)))
}
registers["PC"] = 0
program = list(map(int, re.findall(r"\d+", program)))
out = []

coms = {
    0: lambda: 0,
    1: lambda: 1,
    2: lambda: 2,
    3: lambda: 3,
    4: lambda: registers["A"],
    5: lambda: registers["B"],
    6: lambda: registers["C"],
}

ops = {
    0: ("A", lambda com: registers["A"] >> coms[com]()),
    1: ("B", lambda lit: registers["B"] ^ lit),
    2: ("B", lambda com: coms[com]() % 8),
    3: ("PC", lambda lit: registers["PC"] if registers["A"] == 0 else lit - 2),
    4: ("B", lambda _: registers["B"] ^ registers["C"]),
    5: (None, lambda com: out.append(coms[com]() % 8)),
    6: ("B", lambda com: registers["A"] >> coms[com]()),
    7: ("C", lambda com: registers["A"] >> coms[com]()),
}

while True:
    if registers["PC"] < 0 or registers["PC"] > len(program) - 2:
        break
    operation, operand = (
        program[registers["PC"]],
        program[registers["PC"] + 1],
    )
    op = ops[operation]
    dest_register = op[0]
    result = op[1](operand)
    if dest_register is not None:
        registers[dest_register] = op[1](operand)
    registers["PC"] += 2

print(",".join(map(str, out)))
