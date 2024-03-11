n = int(input())
count = 0

for _ in range(n):
    stack = []
    text = input()
    for i in text:
        if not stack:
            stack.append(i)
        elif i == stack[-1]:        
            stack.pop()
        else:
            stack.append(i)
            
    if not stack:
        count += 1
        
print(count)