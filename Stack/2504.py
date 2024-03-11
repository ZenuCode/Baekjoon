word = input()
print(word)
stack = []
ans = 0
tmp = 1

for i in range(len(word)):
    if word[i] == '(':
        stack.append(word[i])
        tmp *= 2
    elif word[i] == '[':
        stack.append(word[i])
        tmp *= 3
    elif word[i] == ')':
        if not stack or stack[-1] == '[':
            ans = 0
            break
        if word[i - 1] == '(':
            ans += tmp
        tmp //= 2
        stack.pop()
    else:
        if not stack or stack[-1] == '(':
            ans = 0
            break
        if word[i - 1] == '[':
            ans += tmp
        tmp //= 3
        stack.pop()

if stack:
    print(0)
else:
    print(ans)