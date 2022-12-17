N = int(input())
A = list(map(int, input().split()))
# どの数字が何個あるかを保存する
dp = {}
for a in A:
  if not a in dp:
    dp[a] = 1
  else:
    dp[a] += 1
# 存在する数字を大きい順に並び替える
l = sorted(list(dp.keys()))
# 出力用の配列
ans = [0] * N
for i in range(len(l)):
  # 大きい数字が何個あるか
  ans[len(l)-i-1] = dp[l[i]]
print(*ans, sep='\n')