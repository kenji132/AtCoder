n,m= map(int, input().split())
L = list(map(int, input().split()))

def f(mid):
  row = 0
  rem = 0
  for i in range(n):
    if rem >= L[i] + 1:
      rem -= (L[i] + 1)
    else:
      row += 1
      rem = mid - L[i]
      if rem < 0:
        return False
  return row <= m

wa = 0
ac = 10**15

while abs(wa-ac) > 1:
  mid = (wa+ac)//2
  if f(mid):
    ac = mid
  else:
    wa = mid

print(int(ac))