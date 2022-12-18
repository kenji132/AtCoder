from collections import deque
N,M = map(int, input().split())

graph = [[] for i in range(N)]
for i in range(M):
  u,v = map(int,input().split())
  u -= 1
  v -= 1
  graph[u].append(v)
  graph[v].append(u)

visit = [-1 for i in range(N)] # 未訪問: -1 訪問済み: 0 or 1

ans = N*(N-1)//2 - M # 結べる全ての線の内結ばれている線を除く

for i in range(N):
  # 訪問済みはスキップ
  if visit[i] != -1:
    continue

  deq = deque([])
  # 未訪問地を0にする
  visit[i] = 0
  cnt = [1,0,0] # cnt[0]: 0の個数, cnt[1]: 1の個数, cnt[2](cnt[-1]): -1の個数 最初に入れるのは0
  # 訪れた頂点をqueに入れる
  deq.append(i)
  while len(deq) > 0:
    qv = deq.popleft()
    # 取り出した頂点と結ばれている頂点を調べる
    for nv in graph[qv]:
      # 訪問済みの場合
      if visit[nv] != -1:
        # 隣接している頂点の色が同じか？
        if visit[nv] == visit[qv]: # 二部グラフでない場合は0(一本新たに線を追加しても二部グラフにできない)
          print(0)
          exit()
        continue
      # 未訪問の場合 隣接頂点を異なる色にする
      visit[nv] = 1-visit[qv]
      cnt[visit[nv]] += 1
      deq.append(nv)
  # 同じ色を二つ選ぶパターンを削除する
  ans -= cnt[0]*(cnt[0]-1)//2 
  ans -= cnt[1]*(cnt[1]-1)//2


print(ans)