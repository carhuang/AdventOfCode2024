"""
Day 1: Historian Hysteria
With tricks I learned from other solutions
"""

# My original way of reading and parsing the input
with open('./input.txt', 'r') as f:
  lines = f.readlines()
  lines = [entry.strip() for entry in lines]

def _parse_input():
  list_1, list_2 = [], []
  for line in lines:
    entry_1, entry_2 = line.split()
    list_1.append(int(entry_1))
    list_2.append(int(entry_2))
  return [list_1, list_2]

# alternative with list comprehension
data = [int(num) for num in open('input.txt').read().split()]

# alternative with list comprehension, map(), and iterable unpacking
data = [*map(int, open('input.txt').read().split())]

list_1, list_2 = sorted(data[0::2]), sorted(data[1::2])
def part1():
  return sum(map(lambda num_1, num_2: abs(num_1-num_2), list_1, list_2))

def part2():
  # one cons with this approach is that list_2.count(num_1) runs O(N) every round instead of 1 time in my original solution,
  # making this solution O(n^2) instead of O(2N)
  return sum(map(lambda num_1: num_1 * list_2.count(num_1), list_1))

print(part1(), part2())