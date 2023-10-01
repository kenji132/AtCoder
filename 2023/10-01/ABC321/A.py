n = input()
if len(n) > 1:
  for i in range(len(n)-1):
    if int(n[i]) <= int(n[i + 1]):
      print('No')
      exit()
  print('Yes')
else:
  print('Yes')
