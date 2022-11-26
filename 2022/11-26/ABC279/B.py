S = input()
T = input()

len_t = len(T)

if S == T:
  print('Yes')
  exit()
else:
  for i in range(len(S)):
    if S[i:i+len_t] == T:
      print('Yes')
      exit()
  print('No')
