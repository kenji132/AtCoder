s = int(input())
s_history = []
count = 0
while s_history.count(int(s)) == 0:
  s_history.append(int(s))
  if s % 2 == 0:
    s /= 2
  else:
    s = s*3+1
  count += 1

print(count+1)