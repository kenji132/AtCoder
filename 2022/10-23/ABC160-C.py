K,N = map(int, input().split())
A = list(map(int, input().split()))
dis = 0
for i in range(N):
  if i+1 == N:
    dis_c = K - A[i] + A[0]
  else:
    dis_c = A[i+1] - A[i]
  dis = max(dis, dis_c)
print(K - dis)