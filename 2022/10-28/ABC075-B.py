H,W = map(int, input().split())
S = [[0] * (W+2)]
for i in range(H):
  S.append([0] + list(input())+ [0])
S.append([0] * (W+2))
ans_s = S
for i in range(1,H+1):
  for j in range(1,W+1):
    count = 0
    if S[i][j] == "#":
      ans_s[i][j] = "#"
    elif S[i][j] == ".":
      if S[i-1][j] == "#":
        count += 1
      if S[i-1][j+1] == "#":
        count += 1
      if S[i-1][j-1] == "#":
        count += 1
      if S[i][j-1] == "#":
        count += 1
      if S[i][j+1] == "#":
        count += 1
      if S[i+1][j] == "#":
        count += 1
      if S[i+1][j-1] == "#":
        count += 1
      if S[i+1][j+1] == "#":
        count += 1
      ans_s[i][j] = str(count)


for i in range(1,H+1):
  print(''.join([ans_s[i][j] for j in range(1, W+1)]))