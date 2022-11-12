T = [int(input()) for i in range(5)]
T_10 = [ 10 if t%10 == 0 else t%10 for t in T]
last = T[T_10.index(min(T_10))]
ans = 0
cnt = 0
for t in T:
  if t == last and cnt == 0:
    ans += t
    cnt += 1
  elif t % 10 != 0:
    a = 10 - (t % 10)
    ans += (t + a)
  else:
    ans += t
print(ans)