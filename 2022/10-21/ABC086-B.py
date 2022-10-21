import math

A,B = map(str, input().split())
new = int(A + B)
sqrt_1 = math.sqrt(new)
sqrt_2 = int(math.sqrt(new))
if sqrt_1 == sqrt_2:
  print("Yes")
else:
  print("No")