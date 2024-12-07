def parse_input():
    lines = open("input").readlines()
    return [
        (int(test), list(map(int, nums.strip().split(" "))))
        for test, nums in [line.split(":") for line in lines]
    ]
