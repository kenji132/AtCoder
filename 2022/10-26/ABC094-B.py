N,M,X = map(int,input().split())
A = list(map(int, input().split()))
count = 0
for a in A:
  if X < a:
    break
  count += 1

z = M - count
print(min(z, count))
