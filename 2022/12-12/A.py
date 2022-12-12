N = int(input())
P = list(map(int, input().split()))
dp = [[-1]*(10001) for i in range(N+1)]
dp[0][0] = 0
for i in range(N):
  for j in range(10001):
    if dp[i][j] != -1:
      dp[i+1][j] = dp[i][j]
      dp[i+1][j+P[i]] = dp[i][j]

print(dp[N].count(0))

