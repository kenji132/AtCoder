import math

H,W=map(int, input().split())

ans = 0
if H == 1 or W == 1:
  print(1)
elif W % 2 == 0 and H % 2 == 0:
  print(int(H*W/2))
elif W % 2 == 1 and H % 2 == 1:
  print(int(math.floor(H*W/2)+1))
elif (W % 2 == 1 and H % 2 == 0) or( H % 2 == 1 and W % 2 == 0):
  print(int(H*W/2))