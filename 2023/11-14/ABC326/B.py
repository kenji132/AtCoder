n = int(input())
for i in range(n, 920, 1):
  x = i // 100
  y = i % 100 // 10
  if x * y > 9:
    continue
  ans = x * 100 + y * 10 + x * y
  if ans >= n:
    print(ans)
    break

