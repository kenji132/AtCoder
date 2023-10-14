N,K,S = map(int, input().split())

for i in range(N):
  if i < K:
    print(S, end=" ")
  else:
    print(N+2, end=" ")