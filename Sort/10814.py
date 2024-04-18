import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for index in range(n):
    value, string = input().split()
    heapq.heappush(heap, (int(value), index, string))

for _ in range(n):
    value, index, string = heapq.heappop(heap)
    print(value, string)