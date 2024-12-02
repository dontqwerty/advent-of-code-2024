from common import parse_input, check_report

safe_reports = 0
for line in parse_input():
    if check_report(line):
        safe_reports += 1
print(safe_reports)
