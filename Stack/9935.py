import sys

text = input()
bomb = list(input())
stack = []

for i in range(len(text)):
    stack.append(text[i])
    print(stack[-len(bomb):])
    if stack[-len(bomb):] == bomb:
        del stack[-len(bomb):]
        print(stack)

if stack:
    print("".join(stack))
else:
    print("FRULA")