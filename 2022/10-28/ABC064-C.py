N = int(input())
a = list(map(int, input().split()))
s = set()
c = 0
for a_sc in a:
  if a_sc < 3200:
    s.add(a_sc // 400)
  else:
    c += 1
  
print(max(1,len(s)), len(s)+c)
