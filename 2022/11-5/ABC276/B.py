N,M= map(int, input().split())
A = []
B = []
for i in range(M):
  a,b= map(int, input().split())
  A.append(a)
  B.append(b)

dis = []
for i in range(N):
  dis.append([-1])
for m in range(M):
  dis[A[m]-1].append(B[m])
  dis[B[m]-1].append(A[m])

for d in dis:
  num = len(d)-1
  d.sort()
  d.pop(0)
  print(num, *d)