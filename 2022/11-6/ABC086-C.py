import sys

input = sys.stdin.readline
N = int(input())
tp = 0
xp = 0
yp = 0

for i in range(N):
  t,x,y = map(int,input().split())
  dt = t - tp
  dx = abs(x-xp)
  dy = abs(y-yp)
  if (dt+dx+dy)%2 != 0:
    print("No")
    exit()
  if dt < dx+dy:
    print("No")
    exit()
  tp = t
  xp = x
  yp = y

print("Yes")