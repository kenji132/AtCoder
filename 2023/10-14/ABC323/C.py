N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [input() for _ in range(N)]
bonus = [i for i in range(1,N+1)]
score_list = []
not_answers = []
for i in range(N):
  score = i+1
  not_answer = []
  for j in range(M):
    if S[i][j] == "o":
      score += A[j]
    else:
      not_answer.append(A[j])
  score_list.append(score)
  not_answers.append(not_answer)
max_score = max(score_list)
for i in range(N):
  if score_list[i] == max_score:
    print(0)
  else:
    ans = 1
    dif = max_score - score_list[i]
    not_answers[i].sort(reverse=True)
    for j in range(len(not_answers[i])):
      if dif >= not_answers[i][j]:
        ans += 1
        dif -= not_answers[i][j]
      else:
        print(ans)
        break
