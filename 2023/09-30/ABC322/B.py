n,m = map(int, input().split())
s = input()
t = input()

if t[:n] == s and t[m-n:] == s:
  print(0)
elif t[:n] == s and t[m-n:] != s:
  print(1)
elif t[:n] != s and t[m-n:] == s:
  print(2)
else:
  print(3)