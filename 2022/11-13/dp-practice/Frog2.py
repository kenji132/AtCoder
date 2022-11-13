N,K = map(int, input().split())
H = list(map(int, input().split()))
dp=[0]*N


for i in range(N):
  for j in range(1,K+1):
    if i+j < N:
      if dp[i+j] != 0:
        dp[i+j] = min(dp[i]+abs(H[i+j]-H[i]), dp[i+j])
      else:
        dp[i+j] = dp[i]+abs(H[i+j]-H[i])
print(dp[N-1])

