n = int(input())

A = list(map(int, input().split()))
# ans_list = []
# for a in A:
#   if A.count(a) >= 2 and ans_list.count(a) == 0:
#     ans_list.append(a)

# ans_list.sort(reverse=True)
# print(ans_list[0]*ans_list[1] if len(ans_list) >= 2 else 0)

A.sort(reverse=True)
cnt = 1
prev = 0
ans_len = []
for a in A:
  if a == prev:
    ans_len.append(a)
    prev = 0
    if len(ans_len) == 2:
      break
  else:
    prev = a

if len(ans_len) == 2:
  print(ans_len[0]*ans_len[1])
else:
  print(0)