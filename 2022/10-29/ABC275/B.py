A,B,C,D,E,F = map(int, input().split())
L = A*B*C
R = D*E*F
ans = (L-R)%998244353
print(ans)