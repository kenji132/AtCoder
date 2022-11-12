N = int(input())
S = [ list(input()) for i in range(N)]
set_1 = set()
set_0 = set()
cnt = 1
for s in S:
  if s[0] == 'H' or s[0] == 'D' or s[0] == 'C' or s[0] == 'S':
    set_0.add(s[0])
    af_size_0 = len(set_0)
  else:
    print('No')
    exit()
  
  if s[1] == 'A' or s[1] == '2' or s[1] == '3' or s[1] == '4' or s[1] == '5' or s[1] == '6' or s[1] == '7' or s[1] == '8' or s[1] == '9' or s[1] == 'T' or s[1] == 'J' or s[1] == 'Q' or s[1] == 'K':
    set_1.add(s[1])
    af_size_1 = len(set_1)

  else:
    print('No')
    exit()

  for j in range(cnt, N ):
    if s == S[j]:
      print('No')
      exit()
  cnt += 1


print('Yes')