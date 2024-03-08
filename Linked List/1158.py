n, k = map(int, input().split())

arr = [i for i in range(1, n + 1)]
ans = []
pos = 0

while arr:
    pos = (pos + k - 1) % len(arr)
    ans.append(arr.pop(pos))
    
print(str(ans).replace("[", "<").replace("]", ">"))