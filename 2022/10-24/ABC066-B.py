S = list(input())
len_s = len(S)
for i in range(2, len_s, 2):
  if S[0:int((len_s - i)/2 -1)] == S[int((len_s - i)/2):len_s - i - 1]:
    print(len_s - i)
    exit()