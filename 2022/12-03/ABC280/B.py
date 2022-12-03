N = int(input())
S = list(map(int, input().split()))
ans = []
for i in range(N):
  if i == 0:
    ans.append(S[i])
  else:
    ans.append(S[i]-S[i-1])

print(*ans)