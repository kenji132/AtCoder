n,m = map(int, input().split())

graph = [[0] * n for _ in range(n)]

for i in range(m):
  a,b,c = map(int, input().split())
  graph[a-1][b-1] = graph[b-1][a-1] = c

visited = [False] * n
ans = 0
# vが現在地、sが現在地からの距離
def dfs(v,s):
  # vに訪れた印をつける
  visited[v] = True
  global ans
  ans = max(ans,s)
  # vからどこにいけるか全探索
  for i in range(n):
    # iが未訪問かつvからiへの道がある場合
    if not visited[i] and graph[v][i] != 0:
      dfs(i, s+graph[v][i])
  visited[v] = False

for i in range(n):
  dfs(i,0)

print(ans)