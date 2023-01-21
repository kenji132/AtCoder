N,P,Q,R,S= map(int, input().split())
A = list(map(int, input().split()))

ans = []
for i in range(N):
  if i == P-1:
    for a in A[R-1:S]:
      ans.append(a)
    i += len(A[R-1:S])
  elif i > P-1 and i <= Q-1:
    continue
  elif i > R-1 and i <= S-1:
    continue
  elif i == R-1:
    for a in A[P-1:Q]:
      ans.append(a)
    i += len(A[P-1:Q])
  else:
    ans.append(A[i])
print(*ans)