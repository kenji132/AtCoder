N = int(input())
S = input()
cnt_s = [0] * 10
for s in S:
  cnt_s[int(s)] += 1
ans = 0
import math
for i in range(math.ceil(math.sqrt(10**N))):
  a = i**2
  cnt_a = [0] * 10
  while a:
    cnt_a[a%10] += 1
    a //= 10
  for i in range(1, 10):
    if cnt_a[i] != cnt_s[i]:
      break
  else:
    if cnt_a[0] <= cnt_s[0]:
      print(cnt_a, cnt_s)
      ans += 1
print(ans)
