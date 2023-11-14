n,m = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
A.append(10**20)
ans = 0
now = 0
for i in range(n):
  while A[now] < A[i]+m:
    now += 1
  ans = max(ans, now-i)
print(ans)
  