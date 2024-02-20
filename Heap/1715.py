import sys
from heapq import heappush, heappop

def solution():
    n = int(input())
    heap = []

    for _ in range(n):
        heappush(heap, int(sys.stdin.readline()))

    sum = 0
    while len(heap) > 1:
        value = heappop(heap) + heappop(heap)
        sum += value
        heappush(heap, value)

    print(sum)

solution()