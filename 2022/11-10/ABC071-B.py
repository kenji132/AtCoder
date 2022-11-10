S = list(input())
set_S = set()
S.sort()
for s in S:
  set_S.add(s)
li_S = list(set_S)
li_S.sort()
all = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for a in all:
  if a in li_S:
    continue
  else:
    print(a)
    exit()
print('None')
