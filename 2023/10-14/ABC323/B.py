n = int(input())
results = [input() for _ in range(n)]

win_num = [row.count('o') for row in results]

ranking = sorted([(win_num[i], i+1) for i in range(n)], key=lambda x: (-x[0], x[1]))

ans = [player[1] for player in ranking]

print(' '.join(map(str, ans))) 