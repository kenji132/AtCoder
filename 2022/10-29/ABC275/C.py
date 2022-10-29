# S = []

# for i in range(9):
#   S.append(input())
# print(S)
# sharp = []
# i_c = 0
# for sub_s in S:
#   j_c = 0
#   for s in sub_s:
#     if s == "#":
#       sharp.append([i_c, j_c])
#     j_c += 1
#   i_c += 1

# print(sharp)
# dis_list = []
# dis_list_data = []
# for i in range(len(sharp)):
#   for j in range(i+1, len(sharp)):
#     dis = (sharp[i][0] - sharp[j][0])**2 + (sharp[i][1] - sharp[j][1])**2
#     if dis == 2:
#       print(sharp[i][0], sharp[i][1], sharp[j][0], sharp[j][1])
#     dis_list.append(dis)
#     dis_list_data.append([sharp[i],sharp[j]])

# print(dis_list)
# print(dis_list_data)
# counted = set()
# ans = 0
# for i in dis_list:
#   if i in counted:
#     1+1
#   else:
#     if dis_list.count(i)%4 == 0:
#       point = []
#       idx = -1
#       for j in range(dis_list.count(i)):
#         idx = dis_list.index(i, idx+1)
#         if dis_list_data[idx][0] not in point:
#           point.append(dis_list_data[idx][0])
#         if dis_list_data[idx][1] not in point:
#           point.append(dis_list_data[idx][1])
#       print(point)
#       print(len(point))
#       ans += int(dis_list.count(i)/4)
#       print(ans)
#       counted.add(i)
#       print(counted)

# print(ans)

import itertools
S=[input() for _ in range(9)]
ans=0

for i1,j1,i2,j2 in itertools.product(range(9),repeat=4):
  # (i1,j1)から→↓の向きに(i2,j2)がある
  if i2>i1 and j2>=j1 and S[i1][j1]=="#" and S[i2][j2]=="#":
    di=i2-i1
    dj=j2-j1
    i3=i2+dj
    j3=j2-di
    i4=i3-di
    j4=j3-dj
    if 0<=i3<9 and 0<=j3<9 and 0<=i4<9 and 0<=j4<9 and S[i3][j3]=="#" and S[i4][j4]=="#":
      ans+=1
print(ans)
