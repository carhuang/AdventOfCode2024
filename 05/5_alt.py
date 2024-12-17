from itertools import filterfalse
from functools import cmp_to_key

# u/xelf's solution
# split the input into 2 strings; p1 = the rules with '|' replaced by ','; p2 = updates
p1, p2  = open('input.txt').read().replace('|',',').split('\n\n')
# parse the rules into a set that contains all the rules in tuple form; also converts the strings into int
rules   = {*map(eval, p1.splitlines())}
# parse the updates into a list of updates; where each update = a tuple containing pages as int
# eval(x) with x = "17,14,76,84,39" will return a tuple (17, 14, 76, 84, 39)
updates = [*map(eval, p2.splitlines())]

# incorrect(r) takes an update r:tuple and returns an empty set (false) if r is in the right order; else it returns a set of page orderings that are incorrect (true)
# if r = (39,14,13,93,85,66,29,15,52,23,97,69,84,47,87,74,53,76,62,46,49); which is not in the right order
# incorrect(r) = {(46, 49), (97, 69), (52, 23), (39, 14), (15, 52), (47, 87), (76, 62), (13, 93), (84, 47), (74, 53), (85, 66)}
# set(zip(r, r[1:])) constructs a set of tuples (x, y) from the given tuple r; x = an int in r, r[i] and y = the next int, r[i+1]
# set(zip(r, r[1:])) - rules returns a new set with elements in set(zip(r, r[1:])) but not in rules
incorrect = lambda r: set(zip(r, r[1:])) - rules
# midpoint(r) takes a tuple and returns the value of the middle element:int in the tuple
midpoint  = lambda r: r[len(r)//2]
ordered_midpoint = lambda r: midpoint(sorted(r, key=cmp_to_key(lambda a,b: ((a,b) in rules)-1)))

# filterfalse() returns all the correct updates
# map(midpoint, filterfalse(incorrect, updates)) returns all the values of the midpoint element of the correct updates
print('part 1:', sum(map(midpoint, filterfalse(incorrect, updates))))
print('part 2:', sum(map(ordered_midpoint, filter(incorrect, updates))))

# u/4HbQ's solution
from functools import cmp_to_key

rules, pages = open('input.txt').read().split('\n\n')
cmp = cmp_to_key(lambda x, y: -(x+'|'+y in rules))

a = [0, 0]
for p in pages.split():
    p = p.split(',')
    s = sorted(p, key=cmp)
    a[p!=s] += int(s[len(s)//2])

print(*a)