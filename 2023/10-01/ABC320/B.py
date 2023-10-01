s = input()
ans = 1
for i in range(len(s)):
  for j in range(i+1, len(s)+1):
    new_s = s[i:j]
    r_new_s = ''.join(list(reversed(new_s)))
    if new_s == r_new_s and len(new_s) > ans:
      ans = len(new_s)
print(ans)