num = int(input())
X = list(map(int, input().split()))
total = 0
for n in X:
  total += n

avg = round(total/num)
ans = 0
for n in X:
  ans += (n - avg)**2

print(ans)