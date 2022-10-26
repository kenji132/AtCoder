s = input()
count = 0
ans = 0
for i in range(len(s)):
  if s[i] in {"A", "C", "G", "T"}:
    count += 1
    ans = max(ans, count)
  else:
    count = 0

print(ans)