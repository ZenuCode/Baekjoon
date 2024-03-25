import heapq

def solution():
    k, n = map(int, input().split())
    init = list(map(int, input().split()))
    heap = []

    for i in init:
        heapq.heappush(heap, i)

    for _ in range(n):
        lowest = heapq.heappop(heap)
        for i in range(k):
            temp = lowest * init[i]
            print(temp, init[i])
            heapq.heappush(heap, temp)

            if lowest % init[i] == 0:
                break

    print(lowest)

solution()