N,T = map(int, input().split())
li_T = list(map(int, input().split()))
# print(li_T)
ans = 0
for i in range(N):
  print(ans)
  if i == N -1:
    ans += T
  else:
    print(li_T[i+1]-li_T[i])
    if T > li_T[i+1]-li_T[i]:
      ans += li_T[i+1]-li_T[i]
    else:
      ans += T


print(ans)