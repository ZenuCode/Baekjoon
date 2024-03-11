import sys

arr = list(map(str, sys.stdin.readline().rstrip()))
total = 0
stack = []

for i in range(len(arr)):
    if arr[i] == '(':
        stack.append(arr[i])
    elif arr[i] == ')':
        if arr[i-1] == '(':
            stack.pop()
            total += len(stack)
        elif arr[i-1] == ')':  
            stack.pop()
            total += 1

print(total)