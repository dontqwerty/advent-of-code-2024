from common import parse_input


def base3(x):
    y = ""
    while x > 0:
        y = str(x % 3) + y
        x = x // 3
    return y


operators = {
    "0": lambda x, y: x + y,
    "1": lambda x, y: x * y,
    "2": lambda x, y: int(f"{x}{y}"),
}
calibrations = parse_input()
sum = 0
for test, params in calibrations:
    for operations in range(3 ** (len(params) - 1)):
        operations = f"{base3(operations)}".zfill(len(params) - 1)
        result = params[0]
        for slot in range(len(params) - 1):
            result = operators[operations[slot]](result, params[slot + 1])
        if result == test:
            sum += result
            break
print(sum)
