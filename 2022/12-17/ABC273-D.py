H,W,c_r,c_c = map(int, input().split())
c_r -= 1
c_c -= 1
map_l = [['.'] * W for i in range(H)]
map_l[c_r][c_c] = 'T'

N = int(input())
for i in range(N):
  r,c = map(int, input().split())
  map_l[r-1][c-1] = '#'

Q = int(input())
for i in range(Q):
  com, n = input().split()
  n = int(n)
  if com == 'L':
    for i in range(n):
      if c_c-1 >= 0 and map_l[c_r][c_c-1] == '.':
        map_l[c_r][c_c] = '.'
        c_c -= 1
        map_l[c_r][c_c] = 'T'
  elif com == 'R':
    for i in range(n):
      if c_c+1 < H and map_l[c_r][c_c+1] == '.':
        map_l[c_r][c_c] = '.'
        c_c += 1
        map_l[c_r][c_c] = 'T'
  elif com == 'U':
    for i in range(n):
      if c_r-1 >= 0 and map_l[c_r-1][c_c] == '.':
        map_l[c_r][c_c] = '.'
        c_r -= 1
        map_l[c_r][c_c] = 'T'
  elif com == 'D':
    for i in range(n):
      if c_r+1 < H and map_l[c_r+1][c_c] == '.':
        map_l[c_r][c_c] = '.'
        c_r += 1
        map_l[c_r][c_c] = 'T'
  for i in range(H):
    for j in range(W):
      if map_l[i][j] == 'T':
        print(i+1,j+1)