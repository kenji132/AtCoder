S = input()
T = input()
for i in range(len(S)):
  if S[i] != T[i]:
    print(i+1)
    exit()
  elif i == len(S) - 1:
    print(len(S) + 1)
    exit()
