r,g,b,n = map(int, input().split())
r_max = int(n / r)
g_max = int(n / g)
b_max = int(n / b)
ans = 0
for i in range(r_max+1):
  for j in range(g_max+1):
    k = n - (i*r+j*g)
    if k >= 0 and k % b == 0:
      ans += 1

print(ans)

