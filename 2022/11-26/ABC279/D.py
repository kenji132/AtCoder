import math

A,B = map(int, input().split())

i = math.floor((A/2/B)**(2/3))
ans1 = B*(i) + A/math.sqrt(i+1)
ans2 = B*(i+1) + A/math.sqrt(i+2)
print(min(ans1, ans2))

# import math

# A,B = map(int, input().split())

# i = round((A/2/B)**(2/3) - 1)
# if i < 0:
#   i = 0

# ans = B*i + A/math.sqrt(i+1)
# if i != 0:
#   for j in [-1,1]:
#     ans = min(B*(i+j) + A/math.sqrt(i+1+j), ans)
# print('{:.50g}'.format(ans))
