n = int(input())
S = input()

ans = []
flag = False
c = 0
li = -1
for i in range(n):
  if S[i:i+2] == 'na':
    ans.append('n')
    ans.append('y')
    ans.append('a')
    li = i + 1
  elif li == i:
    continue
  else:
    ans.append(S[i])
for s in ans:
  print(s, end ="")