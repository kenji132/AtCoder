K=int(input())
comb=[]
for digit in range(1<<10):
  x=0
  for i in range(9,-1,-1):
    shift_i=1<<i
    if digit & shift_i > 0:
      x *= 10
      x += i
  comb.append(x)
print(sorted(comb)[K+1])