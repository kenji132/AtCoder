x1,y1,x2,y2 = map(int, input().split())
d_x = x2-x1
d_y = y2-y1
x3 = x2 - d_y
y3 = y2 + d_x
x4 = x3 - d_x
y4 = y3 - d_y

print(x3,y3,x4,y4)