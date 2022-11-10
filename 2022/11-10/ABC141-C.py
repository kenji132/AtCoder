N,K,Q = map(int, input().split())
A = [int(input()) for i in range(Q)]
p = [0]*N
for a in A:
  p[a-1] += 1

for i in range(N):
  if K - Q + p[i] <= 0:
    print('No')
  else:
    print('Yes')