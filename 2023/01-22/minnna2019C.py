K,A,B=map(int, input().split())

dif_b = B-K
dif_a = A-K
ans = 1
if dif_b <= dif_a+2:
  ans += K
else:
  dif_a_b = B-A
  ans += A-1
  n = (K-A+1)//2
  m = (K-A+1)%2
  ans += n*dif_a_b+m

print(ans)


