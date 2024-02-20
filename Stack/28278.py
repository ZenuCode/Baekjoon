import sys

testNum = int(input())
stack = []

for i in range(testNum):
    arr = list(map(str, sys.stdin.readline().rstrip().split()))
    if arr[0] == '1':
        stack.append(arr[1])
    elif arr[0] == '2' and stack:
        print(stack.pop())
    elif arr[0] == '3':
        print(len(stack))
    elif arr[0] == '4':
        if stack:
            print(0)
        else:
            print(1)
    elif arr[0] == '5' and stack:
        print(stack[-1])
    else:
        print(-1)