T = int(input())
for i in range(T):
  n = int(input())
  A = list(map(int, input().split()))
  cnt = 0
  for a in A:
    if a%2 != 0:
      cnt += 1 
  print(cnt)