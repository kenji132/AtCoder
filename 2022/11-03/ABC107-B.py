H,W = map(int, input().split())
A = list()
for i in range(H):
  a = list(input())
  A.append(a)

ha = [0]*H
wa = [0]*W
for i in range(H):
  for j in range(W):
    if A[i][j] == "#":
      ha[i] += 1
      wa[j] += 1

for i in range(H):
  if ha[i] == 0:
    continue
  row = ''
  for j in range(W):
    if wa[j] == 0:
      continue
    row += A[i][j]
  print(row)
