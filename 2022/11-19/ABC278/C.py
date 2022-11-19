N,Q = map(int, input().split())

graph = {}
for i in range(Q):
  t,a,b = map(int, input().split())
  if t == 1:
    if not a in graph:
      # setで管理することで高速化できる
      graph[a] = {b}
    else:
      graph[a].add(b)
  elif t == 2:
    if a in graph and b in graph[a]:
        graph[a].remove(b)
  elif t == 3:
    if b in graph and a in graph and a in graph[b] and b in graph[a]:
        print("Yes")
    else:
        print("No")