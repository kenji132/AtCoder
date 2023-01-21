from collections import deque

n,a,b = map(int, input().split())
s = input()
que = deque()
for _ in s:
  que.append(_)


cnt = []
for i in range(n):
  t = 0
  for j in range(n//2):
    if que[j] == que[n-j-1]:
      t += 1
  cnt.append(t)
  v = que.popleft()
  que.append(v)

X = cnt.index(max(cnt))+1
Y = n//2-X
i= 0
ans_l = []
for c in cnt:
  x = i
  y = n//2-c
  ans = x*a+y*b
  ans = min(n//2*b, x*a+y*b)
  ans_l.append(ans)
  i+=1
print(min(min(ans_l),n//2*b))