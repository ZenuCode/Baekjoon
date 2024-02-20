import sys
from heapq import heappush, heappop

def solution():
    input = sys.stdin.readline
    n = int(input())
    heap = []
    for _ in range(n):
        val = int(input())
        if val:
            heappush(heap, (abs(val), val))
        else:
            if heap:
                print(heappop(heap)[1])
            else:
                print(0)

solution()