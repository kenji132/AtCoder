from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under


N = int(input())
A = list(map(int, input().split()))

dp = {}
cnt = 0
for a in A:
  if not a in dp:
    dp[a] = 1
  else:
    dp[a] += 1
# print(dp)
total = 0
for d in dp:
  total += dp[d]*(dp[d]-1)//2

set_a = set(A)
# print(set_a)
for a in A:
  ans = total - dp[a] + 1
  print(ans)

