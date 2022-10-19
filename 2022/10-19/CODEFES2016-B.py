N, A, B = map(int, input().split())
num = A+B
str = input()
passed = 0
B_count = 0
for s in str:
  if s == 'c':
    print("No")
  elif s == 'a':
    if passed < num:
      print('Yes')
      passed += 1
    else:
      print('No')
  elif s == 'b':
    if (B_count < B) and (passed < num):
      print('Yes')
      B_count += 1
      passed += 1
    else:
      print('No')
