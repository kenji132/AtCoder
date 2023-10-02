n,h,x= map(int, input().split())
P= list(map(int,input().split()))
for p in P:
  if h + p >= x:
    print(P.index(p)+1)
    exit()