S = input()
T = input()

len_s = len(S)
len_t = len(T)

dp = [[0] * (len_t+1) for i in range(len_s+1)]
print(dp)
for i in range(len_s):
  for j in range(len_t):
    print(i,j)
    if S[i] == T[j]:
      dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+1)
    dp[i+1][j+1] = max(dp[i+1][j+1], dp[i+1][j])
    dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j+1])
print(dp)

ans = ''
i = len_s
j = len_t
while (i > 0 and j > 0):
  if dp[i][j] == dp[i-1][j]:
    i -= 1
  # (i, j-1) -> (i, j) と更新されていた場合
  elif dp[i][j] == dp[i][j-1]:
    j -= 1
  # (i-1, j-1) -> (i, j) と更新されていた場合
  else:
    ans = S[i-1] + ans
    i -= 1
    j -= 1

  print(ans)