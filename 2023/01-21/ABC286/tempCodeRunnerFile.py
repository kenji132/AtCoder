from collections import deque

n,a,b = map(int, input().split())
s = input()
que = deque()
for _ in s:
  que.append(_)

cnt = []
for i in range(n):
  v = que.popleft()
  que.append(v)
  t = 0
  for j in range(n//2):
    if que[j] == que[n-j-1]:
      t += 1
  cnt.append(t)

X = cnt.index(max(cnt))+1
Y = n//2-X

ans = min(n//2*b, X*a+Y*b)
print(ans)