A,B,C = map(int, input().split())

count = 0
while A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
  temp_A = (B/2)+(C/2)
  temp_B = (A/2)+(C/2)
  temp_C = (A/2)+(B/2)
  A = temp_A
  B = temp_B
  C = temp_C
  count += 1
  if A == B == C:
    count = -1
    break

print(count)
