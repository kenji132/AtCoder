from collections import deque
N,M = map(int, input().split())

graph = {}
for i in range(M):
  u,v = map(int,input().split())
  if not u in graph:
    graph[u] = [v]
  else:
    graph[u].append(v)
  if not v in graph:
    graph[v] = [u]
  else:
    graph[v].append(u)

print(graph)

color = [-1 for i in range(N)]
for i in range(N):
  if color[i] != -1: continue
  deq = deque([])
  color[i] = 0
  deq.append(i)
  while len(deq) > 0:
    qv = deq.popleft()
    for nv in graph[qv]:
      if color[nv] != -1:
        if color[nv] == color[qv]:
          ans = 'No'
          continue
      color[nv] = 1-color[qv]
      deq.append(nv)
