n = int(input())

score = [[] for _ in range(n)]
for i in range(n):
  f,s = map(int,input().split())
  score[f-1].append(s)

ans = 0
for i in range(n):
  if len(score[i]) >= 2:
    score[i].sort()
    c = score[i][-1] + score[i][-2]//2
    ans = max(ans, c)

dif = []
for i in range(n):
  if score[i] != []:
    dif.append(max(score[i]))
dif.sort()
if len(dif) != 1:
  ans = max(ans, dif[-1]+dif[-2])
print(ans)