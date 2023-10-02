n,d,p = map(int, input().split())
f = list(map(int, input().split()))
f.sort(reverse=True)
ans = 0
for i in range(0, n, d):
  c = sum(f[i:i+d])
  if c >= p:
    ans += p
  else:
    ans += c
print(ans)