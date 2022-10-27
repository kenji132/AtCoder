X = int(input())

p = [0] * (10**6)
p[0] = 1
p[1] = 1

for i in range(10**6):
    if p[i] == 1:
        continue
    if i >= X:
        print(i)
        exit()
    for j in range(i*i, 10**6, i):
        p[j] = 1