import sys
input = sys.stdin.readline

n, m = map(int, input().split())
heavy = [[] for _ in range(n+1)]
light = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    heavy[b].append(a) # 현재에서 더 무거운거를 확인
    light[a].append(b) # 더 가벼운거를 확인하기 위해

def heavyBFS(marble):
    visited = [False for _ in range(n+1)]
    visited[marble] = True
    que = [marble]
    while que:
        currM = que.pop(0)
        for each in heavy[currM]:
            if visited[each] == False:
                visited[each] = True
                que.append(each)

    sumVal = 0
    for each in visited:
        if each == True:
            sumVal += 1
    return sumVal

def lightBFS(marble):
    visited = [False for _ in range(n+1)]
    visited[marble] = True
    que = [marble]
    while que:
        currM = que.pop(0)
        for each in light[currM]:
            if visited[each] == False:
                visited[each] = True
                que.append(each)

    sumVal = 0
    for each in visited:
        if each == True:
            sumVal += 1
    return sumVal

res = 0
for i in range(1, n+1):
    lighter = lightBFS(i)
    heavier = heavyBFS(i)
    mid = (n+1) // 2
    if lighter > mid or heavier > mid:
        res += 1
print(res)