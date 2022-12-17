N = int(input())
s = list(input())

com_cnt = 0
for i in range(N):
  if s[i] == '"':
    com_cnt += 1
  if com_cnt % 2 == 0:
    if s[i] == ',':
      s[i] = '.'
print(*s, sep='')
  
