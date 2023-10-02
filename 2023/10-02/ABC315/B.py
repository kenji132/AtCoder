m = int(input())

D = list(map(int, input().split()))

half = (sum(D)+1)//2

a = 1
b = 1
for d in D:
  if half > d:
    half -= d
    a += 1
  elif half == d:
    b = half
    break
  else:
    b = half
    break

print(a,b)