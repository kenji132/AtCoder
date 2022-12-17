N,M = map(int, input().split())
S = []
for i in range(N):
  s = input()
  S.append(s)

cnt = 0
all = 0
for i in range(N):
  for j in range(i+1,N):
    all += 1
    for k in range(M):
      if S[i][k] == 'x' and S[j][k] == 'x':
        cnt += 1
        break

print(all - cnt)