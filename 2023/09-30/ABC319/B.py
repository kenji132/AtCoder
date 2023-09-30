n = int(input())

ans = '1'

for i in range(1, n+1):
  t = ''
  for j in range(1,10):
    if i*j % n == 0:
      t += str(j)
      break
  if not t:
    t = '-'
  ans += t

print(ans)
