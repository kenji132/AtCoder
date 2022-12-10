N,T = map(int, input().split())
A = list(map(int, input().split()))
for i in range(1,len(A)):
  A[i] = A[i]+A[i-1]


d = T % (A[-1])
for i in range(len(A)):
  if A[i] > d:
    if i == 0:
      print(i+1, d)
      exit()
    else:
      print(i+1, d-A[i-1])
      exit()
