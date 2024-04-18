from collections import deque

num = int(input())
arr = list(map(int, input().split()))

big = [-1] * num
stack = deque()

for i in range(num):
    while stack and (stack[-1][0] < arr[i]):
        temp, index = stack.pop()
        big[index] = arr[i]
    stack.append([arr[i], i])

print(*big)