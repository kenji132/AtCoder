# import math

# def prime_factorize(n):
#     a = []
#     while n % 2 == 0:
#         a.append(2)
#         n //= 2
#     f = 3
#     while f * f <= n:
#         if n % f == 0:
#             a.append(f)
#             n //= f
#         else:
#             f += 2
#     if n != 1:
#         a.append(n)
#     return a


# N = int(input())
# A = list(map(int, input().split()))
# ANS_2 = []
# ANS_3 = []

# for a in A:
#   l = prime_factorize(a)
#   ans_2 = l.count(2)
#   ans_3 = l.count(3)
#   print(l)
#   if ans_2 + ans_3 < len(l):
#     print(-1)
#     exit()
#   ANS_2.append(ans_2)
#   ANS_3.append(ans_3)

# print(max(ANS_2)+max(ANS_3))

import math
n = int(input())
a = [*map(int,input().split())]
g,cnt = 0,0
for i in a: 
  g=math.gcd(g,i)
for i in range(n):
    a[i]//=g
    while a[i]%2==0: a[i]//=2; cnt+=1
    while a[i]%3==0: a[i]//=3; cnt+=1
    if a[i]!=1: exit(print(-1))
print(cnt)

