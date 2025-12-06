inp = [list(map(int, row)) for row in open('inp.txt').read().split('\n')]

LENGTH = 12

def solve(bank, depth):  
  record = -1
  idx = -1
  takeFromBack = -LENGTH+depth+1
  if takeFromBack >= 0:
    takeFromBack = 99999999999
  for i, joltage in enumerate(bank[:takeFromBack]):
    if joltage > record:
      record = joltage
      idx = i

  # print(bank, depth)
  # print(record, idx)
  # print('---')

  if depth >= LENGTH - 1:
    return record

  return int(f"{record}{solve(bank[idx+1:], depth+1)}")

# print(solve(inp[1], 0))

c = 0
for bank in inp:
  s = solve(bank, 0)
  c+=s

print(c)

# 811111111111119