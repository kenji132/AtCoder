N, Q = map(int, input().split())
S = input()
problems = [list(map(int, input().split())) for _ in range(Q)]

acc = [0] * N
for i in range(1, N):
  acc[i] = acc[i - 1] + (S[i] == S[i - 1])

for l, r in problems:
    print(acc[r - 1] - acc[l - 1])