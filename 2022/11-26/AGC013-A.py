N = int(input())
A = list(map(int, input().split()))
is_increase = 0
ans = 1
total_d = 0
total_l = [0]
A.append(A[N-1])
for i in range(N):
  total_d += A[i+1] - A[i]
  total_l.append(total_d)
  if total_l[i+1] - total_l[i] > 0:
    if is_increase == -1:
      ans += 1
      is_increase = 0
      continue
    is_increase = 1
  elif total_l[i+1] - total_l[i] < 0:
    if is_increase == 1:
      ans += 1
      is_increase = 0
      continue
    is_increase = -1

print(ans)


