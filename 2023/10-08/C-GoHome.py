import math

x = int(input())
ans = x
m = int(math.sqrt(2*x))

if m*(m+1)/2 >= x:
  ans = m
else:
  ans = m+1

print(ans)