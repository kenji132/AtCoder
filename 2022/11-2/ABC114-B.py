S = list(input())
for i in range(len(S)):
  S[i] = int(S[i])

ans = 10**10
for i in range(len(S)-2):
  num = abs(S[i] * 100 + S[i+1] * 10 + S[i+2] - 753)
  ans = min(ans, num)
print(ans)