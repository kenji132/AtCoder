N,M = map(int, input().split())

G = [[] for i in range(N)]
visited = [False for i in range(N)]

def dfs(i):
  visited[i] = True
  for g in G[i]:
    if visited[g]:
      continue
    else:
      dfs(g)

#隣接リスト作成
for i in range(M):
  u,v = map(int, input().split())
  u-=1
  v-=1
  G[u].append(v)
  G[v].append(u)

cnt = 0

for i in range(N):
  if visited[i]:
    continue
  else:
    cnt += 1
    dfs(i)

print(cnt)