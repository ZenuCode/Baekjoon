import sys
text = sys.stdin.readline().rstrip()
print(text)
stack = []
tmp = 1
ans = 0

for i in text:
    if i == "(":
        stack.append(i)
        tmp *= 2
    elif i == "[":
        stack.append(i)
        tmp *= 3
    elif i == ")":
        if not stack or stack[-1] == '[':
            ans = 0
            break
        if i == "(":
            ans += tmp
        tmp //= 2
        stack.pop()
    elif i == "]":
        if not stack or stack[-1] == '(':
            ans = 0
            break
        if i == "[":
            ans += tmp
        tmp //= 3
        stack.pop()

if stack:
    print(0)
else:
    print(ans)