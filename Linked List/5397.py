def solution():
    n = int(input())
    for _ in range(n):
        stack1 = []
        stack2 = []
        text = input()

        for i in text:
            if i == "<":
                if stack1:
                    stack2.append(stack1.pop())
            elif i == ">":
                if stack2:
                    stack1.append(stack2.pop())
            elif i == "-":
                if stack1:
                    stack1.pop()
            else:
                stack1.append(i)

        stack1.extend(reversed(stack2))
        print("".join(stack1))

solution()