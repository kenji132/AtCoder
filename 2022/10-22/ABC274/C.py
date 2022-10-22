N = int(input())
A = list(input().split())
new_a = []
for a in A:
  new_a.append(int(a))

count = [0] * (2*N+1)
for i in range(N):
  k = new_a[i]
  count[2*(i+1)-1] = count[k-1]+1
  count[2*(i+1)+1-1] += count[k-1]+1

for i in count:
  print(i)