import itertools
N = int(input())
l = list(range(1,N+1))
X = [list(i) for i in itertools.permutations(l)]
P = list(map(int,input().split()))
Q = list(map(int,input().split()))
a,b = X.index(P),X.index(Q)
print(abs(a-b))
