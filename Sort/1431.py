import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    val = input().rstrip()
    valSum =  0
    for i in val:
        if i.isdigit():
            valSum += int(i)
    heapq.heappush(heap, (len(val), valSum, val))

for _ in range(n):
    print(heapq.heappop(heap)[2])
