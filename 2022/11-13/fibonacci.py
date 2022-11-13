n = int(input())
F = [0] * 10**5
def fibo(x):
  if x == 0 or x == 1:
    F[x]= 1
    return F[x]
  if F[x] != 0: # 過去に計算したものがあればそれを出力(動的計画法)
    return F[x]
  F[x] = fibo(x-1) + fibo(x-2)
  print(F[x])
  return F[x]

print(fibo(n))

