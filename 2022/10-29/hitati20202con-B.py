A,B,M = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))
ans = min(A_list) + min(B_list)
for i in range(M):
  x,y,c = map(int, input().split())
  ans = min(ans, A_list[x-1] + B_list[y-1] - c)
print(ans)