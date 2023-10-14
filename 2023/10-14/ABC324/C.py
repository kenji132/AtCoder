N,T_prime = input().split()
N = int(N)

candidates = []
#一文字ずつ確認していき、長さが違えば一方だけ進める
for id in range(N):
  s = input()
  if abs(len(s) - len(T_prime)) > 1:
    continue
  i = 0
  j = 0
  m = 0
  while i < len(s) and j < len(T_prime):
    if s[i] == T_prime[j]:
      i += 1
      j += 1
      m += 1
    elif len(s) > len(T_prime):
      i += 1
    elif len(s) < len(T_prime):
      j += 1
    else:
      i += 1
      j += 1
  if m >= max(len(s), len(T_prime))-1:
      candidates.append(id+1)
print(len(candidates))
print(*candidates)