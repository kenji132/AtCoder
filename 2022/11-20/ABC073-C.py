n = int(input())
A = []
for i in range(n):
  a = int(input())
  A.append(a)

dp = {}
for a in A:
  if not a in dp:
    dp[a] = 1
  elif dp[a] == 0:
    dp[a] = 1
  elif dp[a] == 1:
    dp[a] = 0

ans = 0
for d in dp:
  if dp[d] == 1:
    ans += 1
print(ans)