# n,q = map(int, input().split())
# S = input()
# l_list = []
# r_list = []
# for i in range(q):
#   l,r = map(int, input().split())
#   l_list.append(l)
#   r_list.append(r)

# li = []
# i = 0
# for i in range(n-1):
#   if S[i] == S[i+1]:
#     li.append(i+1)


# for i in range(q):
#   l = l_list[i]
#   r = r_list[i]
#   cnt = 0
#   for j in range(len(li)):
#     if l <= li[j] < r:
#       cnt += 1
#   print(cnt)




# def preprocess(s):
#     n = len(s)
#     acc = [0] * n
#     for i in range(1, n):
#         acc[i] = acc[i - 1] + (s[i] == s[i - 1])
#     return acc

N, Q = map(int, input().split())
S = input()
problems = [list(map(int, input().split())) for _ in range(Q)]

acc = [0] * N
for i in range(1, N):
  acc[i] = acc[i - 1] + (S[i] == S[i - 1])

for l, r in problems:
    print(acc[r - 1] - acc[l - 1])