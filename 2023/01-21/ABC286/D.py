N,x = map(int, input().split())

dp = [[-1]*(x+1) for _ in range(N+1)]
dp[0][0] = 0
# i種類のコインを使ってbに到達できるか？
for i in range(1, N+1):
  A,B = map(int, input().split())
  for b in range(x+1):
    for j in range(B+1):
      # 指定金額以下かつ一種類前の時点でbを達成してるか？
      if b+(A*j) <= x and dp[i-1][b] != -1:
        dp[i][b+(A*j)] = 1
    
if dp[-1][-1] == 1:
  print('Yes')
else:
  print('No')
