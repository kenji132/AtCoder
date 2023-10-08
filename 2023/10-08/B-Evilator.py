S = input()
ans = 0
remain = len(S)
passed = 0
for i in range(1,len(S)+1):
  remain -= 1
  if S[i-1] == 'U':
    ans += remain + 2*passed
  elif S[i-1] == 'D':
    ans += passed + 2*remain
  passed += 1

print(ans)