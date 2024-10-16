import sys
import heapq

input = sys.stdin.readline

def sync_heaps(min_heap, max_heap, valid):
    while min_heap and not valid[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not valid[max_heap[0][1]]:
        heapq.heappop(max_heap)

def solve():
    t = int(input())
    
    for _ in range(t):
        k = int(input())
        min_heap = []
        max_heap = []
        valid = {}
        idx = 0
        
        for _ in range(k):
            action, value = input().split()
            value = int(value)
            
            if action == 'I':
                heapq.heappush(min_heap, (value, idx))
                heapq.heappush(max_heap, (-value, idx))
                valid[idx] = True
                idx += 1
            else:
                if value == 1:
                    sync_heaps(min_heap, max_heap, valid)
                    if max_heap:
                        valid[max_heap[0][1]] = False
                        heapq.heappop(max_heap)
                elif value == -1:
                    sync_heaps(min_heap, max_heap, valid)
                    if min_heap:
                        valid[min_heap[0][1]] = False
                        heapq.heappop(min_heap)

        sync_heaps(min_heap, max_heap, valid)
        if min_heap and max_heap:
            print(-max_heap[0][0], min_heap[0][0])
        else:
            print("EMPTY")

solve()
