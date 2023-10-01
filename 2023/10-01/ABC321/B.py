n,x = map(int, input().split())
A = list(map(int, input().split()))

init_score = sum(A) - max(A) - min(A)
dif = x - init_score
if dif <= min(A):
  print(0)
elif dif <= max(A):
  print(dif)
else:
  print(-1)
