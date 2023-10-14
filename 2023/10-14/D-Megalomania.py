n = int(input())

ab = sorted([[*map(int, input().split())] for _ in range(n)], key=lambda x: x[1])

t = 0
for i in range(n):
  if t + ab[i][0] <= ab[i][1]:
    t += ab[i][0]
  else:
    print("No")
    exit()
print("Yes")