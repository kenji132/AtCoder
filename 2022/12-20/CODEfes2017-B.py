N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

if N < M:
  print('NO')
  exit()

D.sort()
T.sort()
dp = {}
for d in D:
  if not d in dp:
    dp[d] = 1
  else:
    dp[d] += 1

for t in T:
  if t in dp:
    if dp[t] == 0:
      print('NO')
      exit()
    else:
      dp[t] -= 1
  else:
    print('NO')
    exit()

print('YES')


