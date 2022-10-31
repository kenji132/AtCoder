import math
N = int(input())
A = list(map(int, input().split()))
gcd = A[0]
for a in A:
  gcd = math.gcd(gcd,a)

print(int(math.log2(gcd)))
