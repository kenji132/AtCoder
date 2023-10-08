n,p = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0]*2 for _ in range(n+1)]
dp[0][0] = 1

for i in range(n):
  dp[i+1][0] = dp[i][0]
  dp[i+1][1] = dp[i][1]
  if A[i] % 2 == 0:
    dp[i+1][0] += dp[i][0]
    dp[i+1][1] += dp[i][1]
  else:
    dp[i+1][0] += dp[i][1]
    dp[i+1][1] += dp[i][0]
print(dp[n][p])