n, c = map(int, input().split())
m = int(input())
boxes = [list(map(int, input().split())) for _ in range(m)]
boxes.sort(key=lambda x : x[1])
res = 0
upBound = [c] * (n + 1)

for i in range(m):
    temp = c
    for j in range(boxes[i][0], boxes[i][1]):
        temp = min(temp, upBound[j])
    temp = min(temp, boxes[i][2])
    
    for k in range(boxes[i][0], boxes[i][1]):
        upBound[k] -= temp
    
    res += temp

print(res)