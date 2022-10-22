H,W = map(int, input().split())
B = []
for i in range(H):
  b = list(input())
  B.append(b)
ANS = []
for i in range(W):
  count = 0
  for j in range(H):
    if B[j][i] == "#":
      count += 1

  ANS.append(count)

print(' '.join([str(i) for i in ANS]))