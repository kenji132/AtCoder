
n = int(input())
s = input()

for i in range(n):
  if s[i:i+3] == "ABC":
    print(i+1)
    exit()
print(-1)
