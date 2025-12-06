inp = open('inp.txt').read().split('\n\n')

ranges = [tuple(map(int,x.split('-'))) for x in inp[0].split('\n')]

ids = list(map(int,inp[1].split('\n')))

c=0
for id in ids:
  for lb,ub in ranges:
    if id in range(lb,ub+1):
      c +=1
      break
print(c)

print("PART2")

import random

def iteration(ranges):
  combinedRanges = [ranges[0]]
  for nlb, nub in ranges[1:]:
    for i, (lb, ub) in enumerate(combinedRanges):
      r = range(lb,ub+1)
      if nlb <= lb and nub >= ub:
        combinedRanges[i] = (nlb, nub)  
        break
      elif nlb in r and nub > ub:
        combinedRanges[i] = (lb, nub)
        break
      elif nub in r and nlb < lb:
        combinedRanges[i] = (nlb, ub)
        break
    else:
      combinedRanges.append((nlb,nub))
  return combinedRanges

def hasOverlap(ranges):
  for i, (low1, up1) in enumerate(ranges[:-1]):
    for (low2, up2) in ranges[i+1:]:
      if not (low1 > up2 or up1 < low2):
        return True
  return False

while True:
  ranges = iteration(ranges)

  if hasOverlap(ranges):
    pass
    random.shuffle(ranges)
  else:
    break

# print(ranges)

c = 0
for lb, ub in ranges:
  c += ub-lb+1
print(c)