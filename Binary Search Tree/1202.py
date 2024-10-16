import heapq
import sys

input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    jewels = [ tuple(map(int, input().split())) for _ in range(n)]
    bags = [ int(input()) for _ in range(k)] 
    jewels.sort()
    bags.sort()
    que = []
    
    totalSum = 0
    index = 0
    
    for bag in bags:
        while index < n and jewels[index][0] <= bag:
            heapq.heappush(que, -jewels[index][1])
            index += 1

        if que:
            totalSum += -heapq.heappop(que) 
            
    print(totalSum)

solve()
