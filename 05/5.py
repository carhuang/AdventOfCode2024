"""
Day 5: Print Queue
"""
from functools import cmp_to_key
from itertools import filterfalse

rules, updates = open('input.txt').read().replace('|', ',').split("\n\n")
rules = {*map(eval, rules.splitlines())}
updates = [[int(n) for n in update.split(',')] for update in updates.splitlines()]

def midpoint(update):
  return update[len(update)//2]

def correct(update):
  for i in range(len(update)-1):
    for j in range(i+1, len(update)):
      if (update[i], update[j]) not in rules: return False
  return True

def reorder(update):
  return sorted(update, key=cmp_to_key(lambda a, b: ((a, b) in rules)-1))

def part1():
  ans = 0
  for update in updates:
    if correct(update):
      ans += midpoint(update)
  return ans

# alternative approach with shorter code; sacrifices space performance
def part1_alt():
  return sum(map(midpoint, filter(correct, updates)))

def part2():
  ans = 0
  for update in updates:
    if not correct(update):
      ans += midpoint(reorder(update))
  return ans

# alternative approach with shorter code; sacrifices space performance
def part2_alt():
  return sum(map(midpoint, map(reorder, filterfalse(correct, updates))))

print(part1())
print(part2())