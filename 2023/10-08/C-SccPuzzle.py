n,m= map(int, input().split())
ans = 0
if m >= n*2:
  ans += n
  m -= n*2
  ans += m//4
elif m < n*2:
  ans += m//2
  n -= m//2

print(ans)