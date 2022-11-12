A = []
for i in range(3):
  A.append(list(map(int, input().split())))

w_dis = []
for i in range(3):
  d = [A[i][1] - A[i][0] , A[i][2] - A[i][1]]
  w_dis.append(d)
  if w_dis.count(d) != 3 and i == 2:
    print("No")
    exit()

h_dis = []
for j in range(3):
  d = [A[1][j] - A[0][j] , A[2][j] - A[1][j]]
  h_dis.append(d)
  if h_dis.count(d) != 3 and j == 2:
    print("No")
    exit()

print("Yes")

