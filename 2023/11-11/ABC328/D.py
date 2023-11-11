def remove_abc(s):
    stack = []
    for char in s:
        if char == 'C' and len(stack) >= 2 and stack[-1] == 'B' and stack[-2] == 'A':
            stack.pop()
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)

S = input()
print(remove_abc(S))
