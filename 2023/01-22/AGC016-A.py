A = input()
B = set(A)
print(B)
ans_list = []
for b in B:
    cnt = 0
    buf = []
    for i in range(len(A)):
        cnt += 1
        if b == A[i]:
            buf.append(cnt-1)
            cnt = 0
    buf.append(cnt)
    # それぞれの文字がどこにあるか初めの文字と終わりの文字から何文字のところにあるかを保存
    ans_list.append(max(buf))
print(min(ans_list))