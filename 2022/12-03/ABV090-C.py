n,m = map(int, input().split())

if n > m:
  tmp = m
  m = n
  n = tmp

if n >= 2 and m >= 2:
  ans = (n-2) * (m-2)
elif n == 1 and m == 1:
  ans = 1
elif n == 1:
  ans = m-2

print(ans)