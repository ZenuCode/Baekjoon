n = int(input())
graph = [[0] * n for _ in range(n)]
graph[0][0] = 1

k = int(input())
for i in range(k):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 2

d = int(input())
dirDict = dict()
for i in range(d):
    a, b = input().split()
    dirDict[int(a)] = b

time = 0
x = 0
y = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
stack = []
stack.append((0,0))
direction = 0

def turn(dir):
    global direction
    if dir == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4

while True:
    time += 1
    x += dx[direction]
    y += dy[direction]

    if x < 0 or x >= n or y < 0 or y >= n:
        break

    if graph[x][y] == 2:
        graph[x][y] = 1
        stack.append((x,y))
        if time in dirDict:
            turn(dirDict[time])
    elif graph[x][y] == 0:
        graph[x][y] = 1
        stack.append((x,y))
        firstX, firstY = stack.pop(0)
        graph[firstX][firstY] = 0
        if time in dirDict:
            turn(dirDict[time])
    else:
        break

print(time)