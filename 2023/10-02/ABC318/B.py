n = int(input())
table = [[0]*100 for _ in range(100)]
for i in range(n):
  xs,xe,ys,ye=map(int,input().split())
  for j in range(xs,xe):
    for k in range(ys,ye):
      table[j][k] = 1

ans = 0

for row in table:
  for r in row:
    if r == 1:
      ans += 1

print(ans)