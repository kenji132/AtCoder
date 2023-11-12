A = []
B = [[],[],[],[],[],[],[],[],[]]
C = [[],[],[],[],[],[],[],[],[]]

for i in range(9):
  a = list(map(int, input().split()))
  A.append(a)
  for j in range(9):
    B[j].append(a[j])
    
for i in range(0,3):
  for j in range(0,3):
    C[0].append(A[i][j])
  for j in range(3,6):
    C[1].append(A[i][j])
  for j in range(6,9):
    C[2].append(A[i][j])
for i in range(3,6):
  for j in range(0,3):
    C[3].append(A[i][j])
  for j in range(3,6):
    C[4].append(A[i][j])
  for j in range(6,9):
    C[5].append(A[i][j])
for i in range(6,9):
  for j in range(0,3):
    C[6].append(A[i][j])
  for j in range(3,6):
    C[7].append(A[i][j])
  for j in range(6,9):
    C[8].append(A[i][j])

for i in range(9):
  if set([1,2,3,4,5,6,7,8,9]) != set(A[i]):
    print("No")
    exit()
  if set([1,2,3,4,5,6,7,8,9]) != set(B[i]):
    print("No")
    exit()
  if set([1,2,3,4,5,6,7,8,9]) != set(C[i]):
    print("No")
    exit()
print('Yes')
  


# 00,01,02 03,04,05 06,07,08
# 10,11,12 13,14,15 16,17,18
# 20,21,22 23,24,25 Ï