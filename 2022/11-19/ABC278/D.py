from collections import defaultdict

def constant_factory(value):
    return lambda: value

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
for i in range(Q):
  print(A)
  q = list(map(int, input().split()))
  if q[0] == 3:
    print(A[q[1]-1])
  elif q[0] == 2:
    A[q[1]-1] += q[2]
  elif q[0] == 1:
    # A = [q[1]]*N
    A = defaultdict(constant_factory(q[1]))