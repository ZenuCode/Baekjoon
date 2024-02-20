import sys
import heapq as hq

def main():
    n = int(input())
    heap = []

    for _ in range(n):
        val = int(sys.stdin.readline())
        if val:
            hq.heappush(heap, val)
        else:
            if heap:
                print(hq.heappop(heap))
            else:
                print(0)

main()
