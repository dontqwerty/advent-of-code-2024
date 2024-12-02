from common import parse_input, check_report

safe_reports = 0
for line in parse_input():
    for i in range(len(line)):
        if check_report(line[:i] + line[i + 1 :]):
            safe_reports += 1
            break
print(safe_reports)
