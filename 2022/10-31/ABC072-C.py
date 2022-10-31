N = int(input())
A = list(map(int, input().split()))
L = [0]*(10**5)
# valueとkeyの入れ替え(どこにあるかLに記述)
for a in A:
  L[a] += 1
ans = 0
for i in range(1, 10**5-1):
  #三つ並びの合計値の最大値を探す
  s = L[i-1]+L[i]+L[i+1]
  ans = max(s, ans)

print(ans)