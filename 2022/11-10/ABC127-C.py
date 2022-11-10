N,M = map(int, input().split())
L = []
R = []
c = 0
for i in range(M):
  l,r = map(int, input().split())
  L.append(l)
  R.append(r)

for i in range(max(L), min(R)+1):
  c += 1
print(c)