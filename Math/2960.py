n, k = map(int, input().split())
arr = [True] * (n + 1)
curr = 2
temp = 2

for i in range(k):
    while arr[temp] == False:
        temp += curr
        if temp > n:
            curr += 1
            temp = curr
    
    arr[temp] = False
    
print(temp)