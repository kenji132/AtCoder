n = int(input())

X = list(map(int, input().split()))

X_sorted = sorted(X)

med_min,med_max = X_sorted[n//2-1],X_sorted[n//2]

for x in X:
  if x <= med_min:
    print(med_max)
  elif x >= med_max:
    print(med_min)