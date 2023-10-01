m = int(input())
S = list(input() for _ in range(3))
ans = 10**5

for i in range(3*m):
  for j in range(3*m):
    for k in range(3*m):
      if i != j and j != k and k != i and S[0][i % m] == S[1][j % m] == S[2][k % m]:
        ans = min(ans, max(i, j, k))
if ans  == 10**5:
  print(-1)
else:
  print(ans)