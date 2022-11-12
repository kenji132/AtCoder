n = int(input())
S = input()
his = [0]
x = 0
for s in S:
  if s == "D":
    x -= 1
  elif s == "I":
    x += 1
  his.append(x)

print(max(his))
