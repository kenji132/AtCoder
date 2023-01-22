n,m= map(int, input().split())

X = list(map(int, input().split()))

X.sort()

dif = []
for i in range(m-1):
  dif.append(X[i+1] -X[i])
dif.sort(reverse=True)

ans=sum(dif[n-1:])
print(ans)