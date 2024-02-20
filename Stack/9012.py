n = int(input())

for i in range(n):
    count = 0
    value = input()
    
    for j in value:
        if j == '(':
            count += 1
        else:
            count -= 1
        
        if count < 0:
            print("NO")
            break

    if count > 0:
        print("NO")
    elif count == 0:
        print("YES")
        