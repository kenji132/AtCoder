from collections import deque

N,K = map(int, input().split())
A = list(map(int, input().split()))
ans = deque()
for a in A:
  ans.append(a)
for i in range(K):
  ans.popleft()
  ans.append(0)
print(*list(ans))