N = int(input())
S = input()
T = input()
ans = 0
for i in range(N):
  # print(S[-(i+1):])
  # print(T[:(i+1)])
  if S[-(i+1):] == T[:(i+1)]:
    ans = len(S[-(i+1):])

print(2*N-ans)


