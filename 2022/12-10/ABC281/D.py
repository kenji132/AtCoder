# N,K,D = map(int, input().split())
# A = list(map(int, input().split()))
# A.sort(reverse=True)
# print(A)
# new_A = A
# for i in range(N):
#   new_A[i] = A[i] % D

# print(new_A)
# for i in range(N):
#   new_A[i]


# n, k, d = map(int, input().split())
# a = list(map(int, input().split()))

# b = [0] * n
# for i in range(n):
#     b[i] = a[i] % d

# dp = [[-1] * d for i in range(k+1)]
# dp[0][0] = 0
# for i in range(n):
#     for j in range(k):
#         for h in range(d):
#             print(h, k-j)
#             if dp[k-j-1][h] > -1:
#                 dp[k-j][(h+b[i]) % d] = max(dp[k-j][(h+b[i]) % d], dp[k-j-1][h] + a[i])

#         print(dp)



N, K, D = map(int, input().split())
A = list(map(int, input().split()))
 
dp = [[-1] * D for _ in range(K+1)]
dp[0][0] = 0
 
for a in A:
    print(a)
    for k in reversed(range(K)):
        print(k)
        for d in range(D):
            print(dp)
            if dp[k][d] == -1:
                continue
            print(k+1,d+a)
            dp[k+1][(d+a)%D] = max(dp[k+1][(d+a)%D], dp[k][d] + a)
print(dp[K][0])