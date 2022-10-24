N = int(input())
A = list(map(int, input().split()))
A_dic = dict()
for i in range(N):
  dict_name = str(i+1)
  dict_value = A[i]
  A_dic[dict_name] = dict_value
A_dic = sorted(A_dic.items(), key=lambda x:x[1])
ans = []
for i in range(N):
  ans.append(A_dic[i][0])
print(' '.join([a for a in ans]))