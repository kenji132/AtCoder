n = int(input())

A = list(map(int, input().split()))
A = [0] + A + [0]
dif = []
total = abs(A[0] - A[1])
for i in range(1,n+1):
  total += abs(A[i] -A[i+1])
  dif.append(abs(A[i-1] - A[i+1]) - abs(A[i-1] - A[i]) - abs(A[i] - A[i+1]))
  
for i in range(n):
  print(total + dif[i])