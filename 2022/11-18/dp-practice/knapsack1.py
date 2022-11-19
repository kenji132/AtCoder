n,w = map(int, input().split())

W = [] # weight
V = [] # value
for i in range(n):
  w_n,v_n = map(int, input().split())
  W.append(w_n)
  V.append(v_n)

dp = [[0]*(w+1) for _ in range(n+1)]

for i in range(1,n+1):
  for j in range(w+1):
    if j - W[i-1] >= 0:
      dp[i][j] = max(dp[i-1][j-W[i-1]]+V[i-1], dp[i-1][j])
    else:
      dp[i][j] = dp[i-1][j]

print(dp[n][w])