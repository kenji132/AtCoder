S = list(input())
ans = len(S)
cnt = 0
flag = True
for i in range(len(S)):
  if flag:
    if i < len(S)-1:
      if S[i] == '0' and S[i+1] == '0':
        flag = False
        cnt += 1
        i += 2
  else:
    flag = True
print(ans -cnt)

