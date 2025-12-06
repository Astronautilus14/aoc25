g = open('inp.txt').read().split('\n')


def iteration(grid):
  removed=0
  ng: list[list[int]] = []

  for y, row in enumerate(grid):
    ng.append([])
    for x, cell in enumerate(row):
      ng[y].append('.')

      if cell == '.':
        continue

      n=0
      for dy in range(-1, 2):
        for dx in range(-1, 2):
          ny, nx = y+dy, x+dx
          if ny < 0 or ny > len(g)-1 or nx < 0 or nx > len(row)-1 or (dx==0 and dy==0):
            pass
          else:
            if g[ny][nx] == '@':
              n+=1
      if n < 4:
        removed+=1
      else:
        ng[y][x] = '@'

  return ng, removed

c = 0
while True:
  ng, removed = iteration(g)
  if removed == 0:
    break
  c += removed
  g = ng

print(c)

