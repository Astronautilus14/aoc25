input = open('./inp.txt', 'r').readlines()

postion = 50
c = 0

for line in input:
  dir = line[0]
  val = int(line[1:])
  if dir == 'L':
    postion -= val
  else:
    postion += val

  postion %= 100

  if postion == 0:
    c += 1

print(c)

postion = 50
c = 0
for line in input:
  dir = line[0]
  val = int(line[1:])

  for _ in range(val):
    if dir == 'L':
      postion -= 1
    else:
      postion += 1

    postion %= 100
    if postion == 0:
      c += 1

  #print(f"{dir}{val} -> {postion} -> {c}")

print(c)
  