A, B = map(int, input().split())
count = 0
while 1+(A-1)*count < B:
  count += 1

print(count)