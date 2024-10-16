import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
que = deque()

for _ in range(n):
    cmd = list(map(str, input().split()))
    if cmd[0] == "push":
        que.append(int(cmd[1]))
    elif cmd[0] == "pop":
        if que: print(que.popleft())
        else: print(-1)
    elif cmd[0] == "size":
        print(len(que))
    elif cmd[0] == "empty":
        if que: print(0)
        else: print(1)
    elif cmd[0] == "front":
        if que: print(que[0])
        else: print(-1)
    elif cmd[0] == "back":
        if que: print(que[-1])
        else: print(-1)
