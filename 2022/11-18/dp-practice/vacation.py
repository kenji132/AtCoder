N = int(input())
from collections import deque

S = []
for i in range(N):
  s = list(map(int, input().split()))
  S.append(s)

dp = [[0,0,0] for _ in range(N)]
for i in range(N):
  if i == 0:
    dp[0] = S[0]
  else:
    for j in range(3):
      dp[i][j] = max(dp[i-1][(j+1)%3]+S[i][j], dp[i-1][(j+2)%3]+S[i][j])
print(max(dp[N-1]))
