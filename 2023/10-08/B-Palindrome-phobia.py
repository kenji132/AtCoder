S = input()

cnt = [0]*3
for s in S:
  if s == 'a':
    cnt[0] += 1
  elif s == 'b':
    cnt[1] += 1
  else:
    cnt[2] += 1

if max(cnt) - min(cnt) <= 1:
    print('YES')
else:
    print('NO')