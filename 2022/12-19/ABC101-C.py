N,K = map(int, input().split())
A = list(map(int, input().split()))

N -= 1
K -= 1
n = 1
while 1+K*n <= N:
  n += 1
print(n)