import sys
import heapq
input = sys.stdin.readline

n = int(input())
minArr = []
maxArr = []
diffMap = {}

for _ in range(n):
    num, diff = map(int, input().split())
    heapq.heappush(minArr, (diff, num))
    heapq.heappush(maxArr, (-diff, -num))
    diffMap[num] = diff

m = int(input())
for _ in range(m):
    cmd = input().split()
    
    if cmd[0] == "add":
        num, diff = int(cmd[1]), int(cmd[2])
        heapq.heappush(minArr, (diff, num))
        heapq.heappush(maxArr, (-diff, -num))
        diffMap[num] = diff
    
    elif cmd[0] == "recommend":
        if cmd[1] == "1":
            while maxArr:
                if -maxArr[0][1] not in diffMap:
                    heapq.heappop(maxArr)
                elif -maxArr[0][1] in diffMap:
                    if -maxArr[0][0] != diffMap[-maxArr[0][1]]:
                        heapq.heappop(maxArr)
                    else:
                        break
            print(-maxArr[0][1])
        
        elif cmd[1] == "-1":
            while minArr:
                if minArr[0][1] not in diffMap:
                    heapq.heappop(minArr)
                elif minArr[0][1] in diffMap:
                    if minArr[0][0] != diffMap[minArr[0][1]]:
                        heapq.heappop(minArr)
                    else:
                        break
            print(minArr[0][1])
    
    elif cmd[0] == "solved":
        num = int(cmd[1])
        del diffMap[num]
