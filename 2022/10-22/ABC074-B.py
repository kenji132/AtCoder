N = int(input())
K = int(input())
B = list(map(int, input().split()))

ans = 0
avg = K/2
for b in B:
  if b > avg:
    ans += abs(K-b)*2
  else:
    ans += abs(b)*2

print(ans)