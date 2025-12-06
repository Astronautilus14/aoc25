f = open('inp.txt', 'r')
line = f.readline().strip()
#line = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
#line = "95-115"
f.close()

ranges = [[int(y) for y in x.split('-')] for x in line.split(',')]


c=0

for lb, ub in ranges:
  for id in range(lb, ub + 1):
    str_id = str(id)

    if len(str_id) % 2 == 1:
      continue

    fst = str_id[:len(str_id)//2]
    snd = str_id[len(str_id)//2:]
    if fst == snd:
      c += id

print(c)

print("PART2")

c=0
for lb, ub in ranges:
  for id in range(lb, ub + 1):
    str_id = str(id)

    for i in range(len(str_id)//2):
      if str_id[:i+1] * (len(str_id)//(i+1)) == str_id:
        c += id
        break
print(c)