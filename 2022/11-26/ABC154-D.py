N,K = map(int, input().split())
P = list(map(int, input().split()))

ex = []
for p in P:
  ex.append((p+1)/2)

ans = sum(ex[:K])
now = sum(ex[:K])
for i in range(N-K):
  # 先頭を引いて一つ後ろを足す
  now = now - ex[i] + ex[i+K] 
  ans = max(now, ans)
print(ans)