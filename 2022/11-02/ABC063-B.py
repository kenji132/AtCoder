S = list(input())
var = set()
for s in S:
  pre = len(var)
  var.add(s)
  aft = len(var)
  if pre == aft:
    print("no")
    exit()

print("yes")