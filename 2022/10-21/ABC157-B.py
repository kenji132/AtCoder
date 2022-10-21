A = [list(map(int, input().split())) for i in range(3)]
N = int(input())
B = [int(input()) for i in range(N)]
bingo = []
bingo.append([A[0][0],A[0][1], A[0][2]])
bingo.append([A[1][0],A[1][1], A[1][2]])
bingo.append([A[2][0],A[2][1], A[2][2]])
bingo.append([A[0][0],A[1][0], A[2][0]])
bingo.append([A[0][1],A[1][1], A[2][1]])
bingo.append([A[0][2],A[1][2], A[2][2]])
bingo.append([A[0][0],A[1][1], A[2][2]])
bingo.append([A[0][2],A[1][1], A[2][0]])
for bin in bingo:
  count = 0
  for b in B:
    if b in bin:
      count += 1
    if count == 3:
      print("Yes")
      exit()
print("No")