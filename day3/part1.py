inp = [list(map(int, row)) for row in open('inp.txt').read().split('\n')]

c = 0
for bank in inp:
  fst = max(bank[:-1])
  idx = bank.index(fst)
  snd = max(bank[idx+1:])
  c += int(f"{fst}{snd}")

print(c)