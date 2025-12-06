g = open('inp.txt').read().split('\n')

c=0
for y, row in enumerate(g):
  for x, cell in enumerate(row):
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
      c+=1
print(c)