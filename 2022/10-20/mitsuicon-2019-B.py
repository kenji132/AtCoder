import math

paid = int(input())
_raw_price = paid / 1.08
# print(n)
raw_price = math.floor(_raw_price)

# print(_raw_price)
# print(raw_price*1.08)

d_n = math.floor(_raw_price) #切り捨て
# print(d_n)
# print(d_n*1.08)
# print(math.floor(d_n*1.08))

# print("-----")
u_n = math.ceil(_raw_price) #切り上げ
# print(u_n)
# print(u_n*1.08)
# print(math.floor(u_n*1.08))
# print(paid)
if paid == math.floor(d_n*1.08):
  print(d_n)
elif paid == math.floor(u_n*1.08):
  print(u_n)
else:
  print(":(")
