# 塗り分けは二部グラフ判定
#再帰回数の上限を増やす
import sys
sys.setrecursionlimit(10**9)

n,m = map(int,input().split())

x = [-1]*n # 訪問しているかのフラグ
graph = [[] for _ in range(n)]

A= list(map(int,input().split()))
B= list(map(int,input().split()))

for i in range(m):
  graph[A[i]-1].append(B[i]-1)
  graph[B[i]-1].append(A[i]-1)

def dfs(v,c):
  x[v] = c
  for i in graph[v]:
    if x[i] == c: # 同じ色の場合
      return False
    if x[i] == -1 and not dfs(i,1-c): # 未訪問かつ訪問後の結果がFalseの場合
      return False
  return True

for i in range(n):
  if x[i] == -1:
    if not dfs(i,0):
      print("No")
      exit()
print("Yes")

# 別解
import networkx as nx

g=nx.Graph()

n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

for i in range(m):
    g.add_edge(a[i],b[i])

print("Yes" if nx.is_bipartite(g) else "No")