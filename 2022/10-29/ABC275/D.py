# N = int(input())
# N_ = N

# history = [[N_]]
# while len(history[0]) != history[0].count(0):
#   for his in history:
#     sub_his = []
#     # print(his)
#     for h in his:
#       if h == 0:
#         sub_his.append(0)
#       else:
#         new_N_2 = h // 2
#         new_N_3 = h // 3
#         sub_his.append(new_N_2)
#         sub_his.append(new_N_3)
#     history= [sub_his]
# print(len(history[0]))
  

N = int(input())
from functools import lru_cache
@lru_cache
def f(x):
  if x == 0:
    return 1
  else:
    return f(x//2)+f(x//3)
  
print(f(N))