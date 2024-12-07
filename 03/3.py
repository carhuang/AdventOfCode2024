"""
Day 3: Mull It Over
"""
import re

program = open('input.txt').read().replace('\n', '')

def part1(program):
  return sum([int(x) * int(y) for x, y in re.findall("mul\((\d{1,3}),(\d{1,3})\)", program)])

def part2(program):
  program_2 = "do()" + program + "don't()"
  program_2 = ''.join(re.findall("do\(\)(.*?)don't\(\)", program_2))
  return part1(program_2)

print(part1(program))
print(part2(program))