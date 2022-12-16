N,K = map(int, input().split())
A = [1]
a = 0
for i in range(N):
  a += int(input())
  A.append(a)

dp = [[10**10]*(N+1) for i in range(N+1)]
# i日目でj回機嫌良くなるために必要な最小勝利数
dp[0][0] = 0
if A[N] == K:
  print(1)
  exit()
for i in range(N):
  for j in range(i+1):
    dp[i+1][j] = min(dp[i][j], dp[i+1][j])
    # min_w // A[i+1] > dp[i][j] // A[i] であれば良い
    # 一つ前の勝利率より大きくなれば良い
    min_w = dp[i][j] * A[i+1] // A[i] + 1
    # 勝率を上回るために最低限必要な勝数
    dp[i+1][j+1] = min(dp[i+1][j+1], min_w)
    # 前の勝数と勝率を上回るために最低限必要な勝数の比較

t = 0
for i in range(N, -1, -1):
  if dp[-1][i] <= K:
    print(i)
    exit()