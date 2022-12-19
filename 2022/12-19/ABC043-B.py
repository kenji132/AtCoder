S = list(input())
ans = []
for s in S:
  if len(ans) == 0:
    if s != 'B':
      ans.append(s)
  else:
    if s != 'B':
      ans.append(s)
    else:
      ans = ans[:-1]

print(*ans, sep='')
