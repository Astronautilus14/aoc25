from functools import reduce

rows = open('inp.txt').read().splitlines()

height = len(rows)-1
widths = []
operators = [rows[-1][0]]

curr=0
for char in rows[-1][1:]:
  if char == ' ':
    curr+=1
  else:
    operators.append(char)
    widths.append(curr)
    curr=0
widths.append(curr+1)

# print(widths)
# print(operators)

c=0
lp=0
for operator, width in zip(operators, widths):
  g=[]
  for row in rows[:-1]:
    g.append(row[lp:lp+width])
  lp+=width+1
  
  verticalNums = []
  for i in range(width):
    n=""
    for row in g:
      n += row[i]
    verticalNums.append(int(n.replace(" ", "")))
  
  if operator == '+':
    c += sum(verticalNums)
  elif operator == '*':
    c += reduce(lambda x, y: x * y, verticalNums)
  else:
    print('?')

print(c)