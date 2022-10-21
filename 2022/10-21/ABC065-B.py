import sys

N = int(input())
a = [int(input())-1 for i in range(N)]

current = 0
for i in range(N):
  current = a[current]
  if current == 1:
    print(i+1)
    exit()
print(-1)


# button_num = 0
# history = []
# count = 0
# history.append(0)
# while button_num != 1:
#   button_num = a[button_num] - 1
#   if button_num in history:
#     print(-1)
#     sys.exit(0)
#   else:
#     history.append(button_num)
#     count += 1

# print(count)
# sys.exit(0)