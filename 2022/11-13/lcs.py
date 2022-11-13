X = ' ' + input()
Y = ' ' + input()
print(X,Y)
dp = dict()
def lcs(x,y):
  maxl = 0
  m = len(x)-1
  n = len(y)-1
  for i in range(m+1):
    dp[i] = [0]
  for j in range(1,n+1):
    dp[0].append(0)
  print(dp)
  for i in range(1,m+1):
    for j in range(1,n+1):
      print(i,j)
      if x[i] == y[j]:
        dp[i].append(dp[i-1][j-1]+1)
      else:
        dp[i].append(max(dp[i-1][j], dp[i][j-1]))
      maxl = max(maxl, dp[i][j])
  return maxl
print(lcs(X,Y))