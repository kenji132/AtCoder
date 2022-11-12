N = int(input())
A = [int(input()) for i in range(N)]
s_A = sorted(A, reverse=True)
max_a = max(A)
cnt_max = A.count(max_a)
if cnt_max == 1:
  for i in range(N):
    if A[i] == max_a:
      print(s_A[1])
    else:
      print(max_a)
else:
  for i in range(N):
    print(max_a)