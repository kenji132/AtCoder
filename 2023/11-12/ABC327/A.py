n = int(input())
S = input()

for i in range(n-1):
  if (S[i] == 'a' and S[i+1] == 'b') or (S[i] == 'b' and S[i+1] == 'a'):
    print("Yes")
    exit()

print('No')