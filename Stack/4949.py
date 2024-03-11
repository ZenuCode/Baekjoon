import sys
input = sys.stdin.readline

while True:
    text = input().rstrip()
    if text[0] == ".":
        break

    stack = []

    for word in text:
        if word == "(" or word == "[":
            stack.append(word)
        elif word == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(")")
                break
        elif word == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                stack.append("]")
                break
    
    if stack:
        print("no")
    else:
        print("yes")
    