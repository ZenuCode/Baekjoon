import sys
input = sys.stdin.readline

n = int(input())
count = 0
stack = []
arr = [int(input()) for _ in range(n)]

for i in arr:
	while stack and stack[-1] <= i:
		stack.pop()
	stack.append(i)
	count += len(stack) - 1
	
print(count)