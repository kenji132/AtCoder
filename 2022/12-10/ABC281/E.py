from collections import deque

N,M,K = map(int, input().split())
A = list(map(int, input().split()))
end = M -1 
print(deque(A[:M]))
d = deque(A[:M])
for i in range(1,N-M+1):
  d.popleft()
  d.append(A[end+i])
  print(d.sort())