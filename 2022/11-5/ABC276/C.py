import itertools
N = int(input())
p = list(map(int,input().split()))
cnt = 1
for i in range(N-1, -1,-1):
  # print(p[i:N])
  cnt += 1
  new = p[i:N]
  af = sorted(new)
  if af == new:
    continue
  else:
    ans = []
    new
    
    ans.append(af[af.index(new[0])-1])
    new.pop(new.index(af[af.index(new[0])-1]))
    while len(new) != 0:
      ans.append(max(new))
      new.pop(new.index(max(new)))
    print(*p[:i], *ans)
    break


