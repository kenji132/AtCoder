N = int(input())
S = input()
ans = 0
for i in range(N):
  ans = max(len(set(S[:i]) & set(S[i:])), ans)
print(ans)