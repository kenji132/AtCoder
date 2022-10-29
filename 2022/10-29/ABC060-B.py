a,b,c = map(int, input().split())
new_a = a
val = set()
while new_a % b != c:
  new_a = (new_a % b)+a
  former = len(val)
  val.add(new_a)
  later = len(val)
  if former == later:
    print("NO")
    exit()
print("YES")
