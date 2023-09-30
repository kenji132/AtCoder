n,m = map(int, input().split())
A = list(map(int, input().split()))
n_A = [0] + A

for i in range(m):
  k = n_A[i+1] - n_A[i] -1
  if k == 0:
    print(0)
  else:
    for i in range(k, -1, -1):
      print(i)
