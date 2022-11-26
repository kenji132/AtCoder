H,W = map(int, input().split())
dp_S = {}
S = list()
num_S = []
for i in range(H):
  s = list(input())
  num_S.append(s.count('#'))
  for i in range(len(s)):
    if s[i] == '#':
      if not i in dp_S:
        dp_S[i] = 1
      else:
        dp_S[i] += 1
    else:
      if not i in dp_S:
        dp_S[i] = 0

  S.append(s)

dp_T = {}
T = list()
num_T = []
for i in range(H):
  t = list(input())
  num_T.append(t.count('#'))
  for i in range(len(t)):
    if t[i] == '#':
      if not i in dp_T:
        dp_T[i] = 1
      else:
        dp_T[i] += 1
    else:
      if not i in dp_T:
        dp_T[i] = 0

  T.append(t)

d_s = list(dp_S.values())
d_t = list(dp_T.values())
if sorted(d_s) == sorted(d_t) and num_T == num_S:
  print('Yes')
else:
  print('No')