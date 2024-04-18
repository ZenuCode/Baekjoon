import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    heapq.heappush(heap, int(input()))

for _ in range(n):
    print(heapq.heappop(heap))