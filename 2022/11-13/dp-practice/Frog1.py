N = int(input())
H = list(map(int, input().split()))

dp = [0] * N

for i in range(1,N):
  if i == 1:
    dp[i]=abs(H[i]-H[i-1])
  elif i >= 2:
    dp[i]=min(dp[i-1]+abs(H[i]-H[i-1]), dp[i-2]+abs(H[i]-H[i-2]))

print(dp[N-1])
  