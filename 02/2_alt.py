data = [[*map(int, l.split())] for l in open('input.txt')]

def safe(report, with_dampener=False):
  # iterate the report from first level to the second last level
    for i in range(len(report)-1):
        # do something if the current level is not bigger than the next level by at least 1 and at most 3
        if not 1 <= report[i]-report[i+1] <= 3:
            # return False if dampener is off; true if the report is safe with the current level or the next level removed; false otherwise
            return with_dampener and any(safe(report[j-1:j] + report[j+1:]) for j in (i,i+1))
    return True

for with_dampener in False, True: print(sum(safe(report, with_dampener) or safe(report[::-1], with_dampener) for report in data))

# iterate 2 times with the problem dampener on and off
for with_dampener in False, True

# test if the report is safe (levels are decreasing)
safe(report, with_dampener)

# test if the report, reversed, is safe (levels are increasing)
safe(report[::-1], with_dampener)

