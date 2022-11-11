H,W = map(int, input().split())
S = ['.'*(W+2)]
S += [f'.{input()}.' for _ in range(H)]
S += ['.'*(W+2)]
for i, s in enumerate(S[1:-1], 1):
  for j, c in enumerate(s[1:-1], 1):
    if c == '#':
      if {S[i-1][j], S[i+1][j], S[i][j-1], S[i][j+1]} == {'.'}:
        print('No')
        exit()
print('Yes')

