inp = [list(map(int, row)) for row in open('inp.txt').read().split('\n')]

LENGTH = 12

def solve(bank, depth):  
  if depth <= 0:
    return ""

  record = -1
  idx = -1
  takeFromBack = -depth+1
  if takeFromBack >= 0:
    takeFromBack = 99999999999
  for i, joltage in enumerate(bank[:takeFromBack]):
    if joltage > record:
      record = joltage
      idx = i

  return f"{record}{solve(bank[idx+1:], depth-1)}"

# print(solve(inp[1], 0))

c = 0
for bank in inp:
  s = int(solve(bank, 12))
  c+=s

print(c)