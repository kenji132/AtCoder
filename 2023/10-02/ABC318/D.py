n = int(input())

graph = [[0]*n for i in range(n)]
for i in range(n-1):
  d = list(map(int, input().split()))
  for j in range(i+1,n):
    graph[i][j] = graph[j][i]= d[j-i-1]

def dfs(used):
  if all(used):
    return 0
  v = used.index(False)
  used[v] = True
  ret = 0
  for i in range(v+1, n):
    if not used[i]:
      used[i] = True
      ret = max(ret, graph[v][i] + dfs(used))
      used[i] = False
  used[v] = False
  return ret

used = [False] * n
ans = 0
if n % 2 == 0:
  ans = max(ans, dfs(used))
else:
  for i in range(n):
    used[i] = True
    ans = max(ans, dfs(used))
    used[i] = False
print(ans)