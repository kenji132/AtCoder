n = int(input())
A = list(map(int, input().split()))
A.sort()
now = A[0]
for a in A:
  if a != now:
    print(now)
    exit()
  now += 1