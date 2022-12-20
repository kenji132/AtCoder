import math
N,K = map(int, input().split())
X = list(map(int, input().split()))
# ans = 10**20
dis = []
for x in X:
  # ans = min(abs(K - x), ans)
  dis.append(abs(K - x))
ans = dis[0]
for d in dis:
  ans = math.gcd(ans, d)
print(ans)