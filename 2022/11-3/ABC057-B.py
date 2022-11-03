N,M = map(int, input().split())
A = []
B = []
C = []
D = []
for i in range(N):
  a,b = map(int, input().split())
  A.append(a)
  B.append(b)

for i in range(M):
  c,d = map(int, input().split())
  C.append(c)
  D.append(d)

for i in range(N):
  ans = 10**10
  id = 0
  for j in range(M):
    dis = abs(A[i] - C[j])+  abs(B[i] - D[j])
    if ans != dis:
      if ans > dis:
        ans = dis
        id = j+1
  print(id)
