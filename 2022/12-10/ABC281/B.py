S = input()
if len(S) == 8:
  if S[0].isalpha() and S[-1].isalpha() and not S[-2].isalpha() and not S[1].isalpha():
    for s in S[1:-1]:
      if s.isalpha():
        print('No')
        exit()
    if S[1] != '0':
      print('Yes')
    else:
      print('No')
  else:
    print('No')
else:
  print('No')

