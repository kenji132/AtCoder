s = list(input())
t = list(input())
s.sort()
t.sort(reverse=True)
if s < t:
  print("Yes")
else:
  print("No")

all =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(len(s)):
  if all.index(s[i]) < all.index(t[i]):
    print('Yes')
    exit()
  elif all.index(s[i]) > all.index(t[i]):
    print('No')
    exit()
  elif i == len(s)-1:
    if all.index(s[i]) == all.index(t[i]):
      if len(s) < len(t):
        print('Yes')
        exit()
      else:
        print('No')
        exit()
  elif i == len(t)-1:
    if all.index(s[i]) == all.index(t[i]):
      if len(s) < len(t):
        print('Yes')
        exit()
      else:
        print('No')
        exit()
