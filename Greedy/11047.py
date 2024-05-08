n, target = map(int, input().split()) 
arr = list(map(int, (input() for _ in range(n))))
count = 0

for i in reversed(range(n)):
    count += target // arr[i]
    target = target % arr[i] 

print(count)