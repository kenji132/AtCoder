N,K = map(int, input().split())
A = list(map(int, input().split()))

dp = {}
for a in A:
  if not a in dp:
    dp[a] = 1
  else:
    dp[a] += 1
siz = len(dp)
dis = siz - K
new_dp = sorted(dp.items(), key=lambda i: i[1])
ans = 0
for i in range(dis):
  ans += new_dp[i][1]

print(ans)