str = str(input())
str_len = len(str)
W_count = 0
ans = 0
for i in range(str_len):
  if str[i] == "W":
    ans += i-W_count
    W_count += 1
print(ans)