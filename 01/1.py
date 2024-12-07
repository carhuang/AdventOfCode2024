"""
Day 1: Historian Hysteria
"""
import collections

# read the input
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

def total_distance(list_1, list_2):
  list_1.sort()
  list_2.sort()
  total = 0
  for i in range(len(list_1)):
    distance = abs(list_1[i]-list_2[i])
    total += distance
  return total

def similarity(list_1, list_2):
  frequency_2 = collections.Counter(list_2)
  similarity_score = 0
  for number in list_1:
    score = number * frequency_2[number]
    similarity_score += score
  return similarity_score

list_1, list_2 = _parse_input()

def part1():
  return total_distance(list_1, list_2)

def part2():
  return similarity(list_1, list_2)

print(part1())
print(part2())