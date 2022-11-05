a = int(input())
b = int(input())
c = int(input())
X = int(input())

ans = 0
for i in range(a+1):
  for j in range(b+1):
    for k in range(c+1):
      cost = 500*i+100*j+50*k
      # print(cost)
      if cost == X:
        ans += 1

print(ans)