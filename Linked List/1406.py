import sys

stack1 = list(input())
stack2 = []
n = int(input())

for _ in range(n):
	cmd = sys.stdin.readline().split()
	if cmd[0] == 'L' and stack1:
		stack2.append(stack1.pop()) 
	elif cmd[0] == 'D' and stack2:
		stack1.append(stack2.pop())
	elif cmd[0] == 'B' and stack1:
		stack1.pop()
	elif cmd[0] == 'P':
		stack1.append(cmd[1])
        
print("".join(stack1 + list(reversed(stack2))))