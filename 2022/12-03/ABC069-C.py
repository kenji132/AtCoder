N = int(input())
A = list(map(int, input().split()))

num_4 = 0
num_2 = 0
num_other = 0
for a in A:
  if a % 4 == 0:
    num_4 += 1
  elif a % 2 == 0:
    num_2 += 1
  else:
    num_other += 1

# print(num_4, num_2, num_other)

if num_4 * 2 + 1 == N:
  print("Yes")
elif num_4 * 2 + num_2 >= N:
  print("Yes")
else:
  print("No")