# Wが大きいと計算量膨大に
N,W = map(int, input().split())

dp = [[0]* (W+1) for i in range(N+1)]

for i in range(1,N+1):
  w,v = map(int, input().split())
  for j in range(W+1):
    if j >= w:
      dp[i][j] = max(dp[i-1][j-w]+v, dp[i-1][j])
    else:
      dp[i][j] = dp[i-1][j]
    print(dp)

# Wではなく、Vに注目する
N,W = map(int, input().split())
max_v = 100100
dp = [[10**10]*max_v for i in range(N+1)]
dp[0][0] = 0
for i in range(1,N+1):
  w,v = map(int, input().split())
  for j in range(max_v):
    if j >= v:
      dp[i][j] = min(dp[i-1][j-v]+w, dp[i-1][j])
    else:
      dp[i][j] = dp[i-1][j]
ans = 0
for i in range(max_v):
  if dp[N][i] <= W:
    ans = i
print(ans)