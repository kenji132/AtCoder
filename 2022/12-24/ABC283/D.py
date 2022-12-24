S = list(input())
left = 0
l_id = []
right = 0
box = []
box_id = [] #入れたときのiを記録
i = 0
for s in S:
  if s == '(':
    left += 1
    l_id.append(i)
  elif s == ')':
    right += 1
    # j = l_id[len(l_id)-1 - (right-1)] + 1
    if box_id != []:
      j = box_id[0]
      if j in box_id:
        b_j = box_id.index(j)
        box = box[:b_j]
        box_id = box_id[:b_j] 
  else:
    if not s in box:
      box.append(s)
      box_id.append(i)
    else:
      print('No')
      exit()
  i += 1

print('Yes')
