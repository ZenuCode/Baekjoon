import sys
from heapq import heappush, heappop

def solution():
    n = int(input())
    heap = []

    for _ in range(n):
        val = int(sys.stdin.readline())
        if val:
            heappush(heap, (-val, val))
        else:
            if heap:
                print(heappop(heap)[1])
            else:
                print(0)

solution()