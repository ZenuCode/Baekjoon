import sys

row, col = list(map(int, sys.stdin.readline().split()))
map = [[0 for x in range(col)] for x in range(row)]
for i in range(row):
    info = sys.stdin.readline()
    for j in range(col):
        map[i][j] = info[j]

route = []
route.append(map[0][0])
maxCount = [1]
currDist = 1

def recurse(x, y, route, currDist):
    if x + 1 < col:
        print(x, y, route, currDist)
        if map[x+1][y] not in route:
            route.append(map[x+1][y])
            recurse(x + 1, y, route, currDist + 1)
            route = route[0: x + y + 1]
            if (currDist > 7):
                return
    if y + 1 < row:
        print(x, y, route, currDist)
        if map[x][y+1] not in route:
            route.append(map[x][y+1])
            recurse(x, y + 1, route, currDist + 1)
            route = route[0: x + y + 1]
            if (currDist > 7):
                return
    if x - 1 >= 0:
        print(x, y, route, currDist)
        if map[x-1][y] not in route:
            route.append(map[x-1][y])
            recurse(x - 1, y, route, currDist + 1)
            route = route[0: x + y + 1]
            if (currDist > 7):
                return
    if y - 1 >= 0:
        print(x, y, route, currDist)
        if map[x][y-1] not in route:
            route.append(map[x][y-1])
            recurse(x, y - 1, route, currDist + 1)
            route = route[0: x + y + 1]
            if (currDist > 7):
                return
    
    if maxCount[0] < currDist:
        maxCount[0] = currDist
    if (currDist > 7):
        return
    

recurse(0,0, route, currDist)

print(maxCount[0])