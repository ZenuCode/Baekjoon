import sys
input = sys.stdin.readline
arr = []

for i in range(int(input())):
    arr.append(int(input()))

arr.sort()
for i in arr:
    print(i)


"""
import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    heapq.heappush(heap, int(input()))

for _ in range(n):
    print(heapq.heappop(heap))



"""