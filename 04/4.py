"""
Day 4: Ceres Search
"""

word_search = open('input.txt').read().split()

def in_bound(x, y):
  return 0 <= x < len(word_search[0]) and 0 <= y < len(word_search)

def is_word(x, y, dir_x, dir_y, word):
  for move in range(1,len(word)):
    next_x, next_y = x + move*dir_x, y + move*dir_y
    if not in_bound(next_x, next_y) or word_search[next_y][next_x] != word[move]: return False
  return True
  
def find_word(word):
  word_count = 0
  for y in range(len(word_search)):
    for x in range(len(word_search[0])):
      if word_search[y][x] == word[0]:
        for dir_x in (-1,0,1):
          for dir_y in (-1,0,1):
            if is_word(x, y, dir_x, dir_y, word): word_count += 1
  return word_count

def is_MAS(x, y, dir):
  if dir == 'L':
    u_x, u_y = x-1, y+1
    d_x, d_y = x+1, y-1
    if not in_bound(u_x, u_y) or not in_bound(d_x, d_y): return False
    return (word_search[u_y][u_x] == 'M' and word_search[d_y][d_x] == 'S') or (word_search[u_y][u_x] == 'S' and word_search[d_y][d_x] == 'M')
  if dir == 'R':
    u_x, u_y = x+1, y+1
    d_x, d_y = x-1, y-1
    if not in_bound(u_x, u_y) or not in_bound(d_x, d_y): return False
    return (word_search[u_y][u_x] == 'M' and word_search[d_y][d_x] == 'S') or (word_search[u_y][u_x] == 'S' and word_search[d_y][d_x] == 'M')

def find_X_MAS():
  word_count = 0
  for y in range(len(word_search)):
    for x in range(len(word_search[0])):
      if word_search[y][x] == 'A':
        if is_MAS(x, y, 'L') and is_MAS(x, y, 'R'): word_count += 1
  return word_count

def part1():
  return find_word('XMAS')

def part2():
  return find_X_MAS()

print(part1())
print(part2())