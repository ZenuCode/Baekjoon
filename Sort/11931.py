import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    heapq.heappush(heap, -int(input()))

for _ in range(n):
    print(-heapq.heappop(heap))



"""
import sys
data = [ 0 ]*2000001
n = int(sys.stdin.readline())
for _ in range(n):
    data[int(sys.stdin.readline())] +=1
    
print("\n".join([str(i) for i in range(1000000, -1000001, -1) if data[i]]))

"""