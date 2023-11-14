x,y = map(int, input().split())
if x - y > 3 or y - x > 2:
  print("No")
else:
  print("Yes")