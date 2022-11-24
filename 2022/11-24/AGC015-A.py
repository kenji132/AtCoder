N,A,B= map(int, input().split())
n = N-2
ans = 0
if N == 1:
  if A == B:
    ans = 1
  else:
    ans = 0
  print(ans)
  exit()
elif N == 2:
  ans = 1
  print(ans)
  exit()
elif N > 2:
  if A == B:
    ans = 1
    print(ans)
    exit()
  elif A > B:
    ans = 0
    print(ans)
    exit()
  else:
    dis = B - A + 1
    ans = dis + (dis - 1)*(n-1)
print(ans)