"""
Day 2: Red-Nosed Reports
"""

# read the input
with open('./input.txt', 'r') as f:
  lines = f.readlines()
  lines = [entry.strip() for entry in lines]

def _parse_input():
  reports = []
  for line in lines:
    levels = [int(number) for number in line.split()]
    reports.append(levels)
  return reports

def is_safe(report):
  for i in range(len(report)-1):
    if not 1 <= report [i+1] - report[i] <= 3: return False
  return True

def is_safe_with_dampener(report):
  for i in range(len(report)-1):
    if not 1 <= report [i+1] - report[i] <= 3:
      return is_safe(report[i-1:i] + report[i+1:]) or is_safe(report[i:i+1] + report[i+2:])
  return True

reports = _parse_input()

def part1():
  return sum(is_safe(report) or is_safe(report[::-1]) for report in reports)

def part2():
  return sum(is_safe_with_dampener(report) or is_safe_with_dampener(report[::-1]) for report in reports)

print(part1())
print(part2())
