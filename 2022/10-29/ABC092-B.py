N = int(input())
d,x = map(int, input().split())
A = []
for i in range(N):
  A.append(int(input()))
m = 0
for a in A:
  m += (d-1) // a + 1
print(m+x)