n = int(input())

D = list(map(int, input().split()))
cnt = 0
for i in range(1, n+1):
  if i < 10 or i % 11 == 0:
    for d in range(1, D[i-1]+1):
      if d < 10:
        if d == i or i % 10 == d:
          cnt += 1
      elif d % 11 == 0:
        if d % 10 == i % 10:
          cnt += 1
print(cnt)