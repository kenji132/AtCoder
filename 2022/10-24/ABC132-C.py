N = int(input())
d = list(map(int, input().split()))
d.sort()
ans = 0
h = int(N/2)
if d[h-1] == d[h]:
  ans = 0
else:
  ans += d[h] - d[h-1]

print(ans)