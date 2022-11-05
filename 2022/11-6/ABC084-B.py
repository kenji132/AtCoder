a,b  =map(int, input().split())
S = input()
if S[a] == "-":
  n = str(S[a+1:])
  m = str(S[:a])
  if n.isdigit() and m.isdigit():
    print("Yes")
    exit()

print("No")