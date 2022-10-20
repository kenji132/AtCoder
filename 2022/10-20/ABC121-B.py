N, M, C=map(int, input().split())
b = list(input().split())
int_b = [int(i) for i in b]

a = []
for i in range(N):
  sub_a = list(input().split())
  int_sub_a = [int(i) for i in sub_a]
  a.append(int_sub_a)

count = 0
for i in range(N):
  ans = C
  for j in range(M):
    ans += int_b[j]*a[i][j]
  
  if ans > 0:
    count += 1

print(count)