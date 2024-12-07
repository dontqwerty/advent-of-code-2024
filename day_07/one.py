from common import parse_input

operators = {"0": lambda x, y: x + y, "1": lambda x, y: x * y}
calibrations = parse_input()
sum = 0
for test, params in calibrations:
    for operations in range(2 ** (len(params) - 1)):
        operations = f"{operations:b}".zfill(len(params) - 1)
        result = params[0]
        for slot in range(len(params) - 1):
            result = operators[operations[slot]](result, params[slot + 1])
        if result == test:
            sum += result
            break
print(sum)
