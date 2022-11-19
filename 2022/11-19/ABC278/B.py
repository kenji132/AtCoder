H,M = map(int, input().split())
flag = True
while flag:
  h_10 = H//10
  h_1 = H%10

  m_10 = M//10
  m_1 = M%10
  #入れ替え
  tmp_m = m_10
  tmp_h = h_1
  m_10 = tmp_h
  h_1 = tmp_m
  h = h_10*10+ h_1
  m = m_10*10+ m_1
  if (m >= 0 and m <= 59) and (h >= 0 and h <= 23):
    flag = False
  else:
    M += 1
    if M == 60:
      H += 1
      M = 0
    if H == 24:
      H = 0

print(H, M)