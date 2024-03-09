import sys
input = sys.stdin.readline

n = int(input())
stack = []
arr = []
count = 0

for i in range(n):
    val = int(input())
    while stack:
        if stack[-1][0] < val:
            count += stack.pop()[1]
        else:
            break
    
    if not stack:
            stack.append([val, 1])
    elif stack[-1][0] == val:
            temp = stack.pop()[1]
            count += temp
            if stack:
                count += 1
            stack.append([val, temp + 1])
           
    else:
        stack.append([val, 1])
        count += 1

print(count)