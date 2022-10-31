import math
H = int(input())
cnt = 0
if H == 1:
  print(1)
  exit()
else:
  while H > 1:
    H /= 2
    math.floor(H)
    cnt += 1
    if H == 1:
      H = 0
      cnt += 1
      break
print(2**cnt-1)