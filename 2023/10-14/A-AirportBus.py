N,C,K = map(int, input().split())
T = [int(input()) for _ in range(N)]
T.sort()
start = T[0] + K
passengers = 1
ans = 0

for i in range(1,N):
  if passengers < C and start >= T[i]:
    passengers += 1
  else:
    passengers = 1
    start = T[i] + K
    ans += 1
print(ans + 1)