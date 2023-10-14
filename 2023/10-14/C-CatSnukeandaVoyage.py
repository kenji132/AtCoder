n,m = map(int, input().split())
dp = [[] for _ in range(n)]
for i in range(m):
  a,b = map(int, input().split())
  dp[a-1].append(b)
  dp[b-1].append(a)

for j in dp[0]:
  if n in dp[j-1]:
    print("POSSIBLE")
    exit()

print("IMPOSSIBLE")
