import sys
from collections import deque
input = sys.stdin.readline

n, l = map(int, input().split())
arr = list(map(int, input().split()))
que = deque([])

for i in range(n):
    if que:
        if que and que[0][0] <= i - l:
            que.popleft()
    
        while que and arr[i] < que[-1][1]:
            que.pop()
    
    que.append((i, arr[i]))
    print(que[0][1], end=" ")