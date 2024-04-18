import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for index in range(n):
    one, two = map(int, input().split())
    heapq.heappush(heap, (one, two))

for _ in range(n):
    one, two = heapq.heappop(heap)
    print(one, two)