from itertools import permutations

table = []
for i in range(3):
  n1,n2,n3 = map(int, input().split())
  table.append(n1)
  table.append(n2)
  table.append(n3)

total = 9*8*7*6*5*4*3*2
disappear = 0

line = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]


for pl in permutations(range(9)):
  ok = False
  for l in line:
    tmp = []
    for p in pl:
      if p in l:
        tmp.append(table[p])
        if len(tmp) == 2:
          if tmp[0] != tmp[1]:
            break
        elif len(tmp) == 3:
          if tmp[1] != tmp[2]:
            ok = True
            disappear += 1
          break
    if ok:
      break

print((total - disappear)/total)


