import copy
K = int(input())

def prime(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

pf = {}
pri = prime(K)
print(pri)
for p in pri:
  if not p in pf:
    pf[p] = 1
  else:
    pf[p] += 1

left = 1
print(pf)
right = K

while left < right:
  center = (left + right) // 2
  for key, value in pf.items():
    print(key, value, center)
    print('----')
    cnt = 0
    tmp = key
    while tmp <= center:
      cnt += center // tmp
      tmp *= key
      print(cnt ,tmp)
    if cnt < value:
        left = center + 1
        print('left')
        break
    else:
        right = center


print(left)
