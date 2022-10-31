N,A,B = map(int, input().split())
if A == 0:
  print(0)
elif A+B < N:
  x = N//(A+B)
  y = N%(A+B)
  if y >= A:
    print(A*x+A)
  else:
    print(A*x+y)
elif A >= N:
  print(N)
elif A+B >= N:
  print(A)

