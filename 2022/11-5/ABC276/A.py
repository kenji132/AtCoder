S = list(input())
cnt = 0
ans = -1
for s in S:
  cnt += 1
  if s == "a":
    ans = cnt

print(ans)
