from collections import deque

N = int(input())
graph = {}
for i in range(N):
  a,b = map(int, input().split())
  if not a in graph:
    graph[a] = [b]
  else:
    graph[a].append(b)
  if not b in graph:
    graph[b] = [a]
  else:
    graph[b].append(a)

print(graph)
start = deque()
start.append(1)
S = {1}
while start:
  v = start.pop()
  for i in graph[v]:
    if not i in S:
      start.append(i)
      S.add(i)
print(max(S))

# n = int(input())
# graph = defaultdict(list)

# for i in range(n):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# start = deque()
# start.append(1)
# S = {1}
# while start:
#   v = start.pop()
#   for i in graph[v]:
#     if not i in S:
#       start.append(i)
#       S.add(i)
# print(max(S))

