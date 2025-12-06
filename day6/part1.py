from functools import reduce

rows = [[y.strip() for y in x.split(' ') if y != ''] for x in open('inp.txt').read().split('\n')]

problems = []

for row in rows[:-1]:
  for i, n in enumerate(row):
    if i in range(len(problems)):
      problems[i].append(int(n))
    else:
      problems.append([int(n)])

c=0
for operator, nums in zip(rows[-1], problems):
  if operator == '+':
    c += sum(nums)
  elif operator == '*':
    c += reduce(lambda x, y: x*y, nums)
print(c)