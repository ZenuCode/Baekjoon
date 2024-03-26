import sys
input = sys.stdin.readline

def backTrack(index):
    if len(stack) == 6:
        print(*stack)
        return
    
    for i in range(index, n):
        stack.append(arr[i])
        backTrack(i + 1)
        stack.pop()

n = 1
while n != 0:
    n, *arr = map(int, input().split())
    stack = []
    backTrack(0)
    print()