W = int(input())
N,K = map(int,input().split())

A = []
B = []
for i in range(N):
  a,b = map(int,input().split())
  A.append(a)
  B.append(b)

#dp[i][k][w]:=i番目までのスクショでk枚使って合計幅がwでの重要度の最大値
dp=[[0]*(W+1) for _ in range(K+1)]
for i in range(N):
    print('----')
    for k in range(K,0,-1):
        for w in range(W, 0, -1):
            if 0<=w-A[i]:
                dp[k][w]=max(dp[k][w], dp[k-1][w-A[i]]+B[i])
        print(dp[0])
        print(dp[1])
        print(dp[2])
        print(dp[3])
