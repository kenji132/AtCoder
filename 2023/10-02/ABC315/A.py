S = input()
ans = ""
for s in S:
  if not s in 'aeiou':
    ans += s

print(ans)