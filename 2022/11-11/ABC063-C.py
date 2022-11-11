n = int(input())
S = [int(input()) for i in range(n)]
ans = sum(S)
if ans % 10 == 0:
  ans = 0

for s in S:
  tmp = sum(S) - s
  if tmp % 10 == 0:
    tmp = 0
  ans = max(ans, tmp)

print(ans)
