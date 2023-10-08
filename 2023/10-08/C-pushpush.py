n = int(input())
A = list(map(int, input().split()))
ans_index = []
if n % 2 == 0:
  for i in range(n, 0, -2):
    ans_index.append(i)
  for i in range(1, n, 2):
    ans_index.append(i)
else:
  for i in range(n, 0, -2):
    ans_index.append(i)
  for i in range(2, n, 2):
    ans_index.append(i)

for i in ans_index:
  print(A[i-1], end=' ')