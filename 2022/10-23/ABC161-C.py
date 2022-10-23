N,K = map(int, input().split())
n = N
while True:
  if n == 0:
    break
  if n < K:
    next_n = abs(n-K)
  else:
    next_n = n%K

  if next_n >= n:
    break
  n = min(n, next_n)

print(n)
