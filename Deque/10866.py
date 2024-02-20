import sys
from collections import deque

def solution():
    n = int(input())
    dque = deque([])
    for _ in range(n):
        cmd = sys.stdin.readline().split()
        if cmd[0] == "push_front":
            dque.appendleft(cmd[1])
        elif cmd[0] == "push_back":
            dque.append(cmd[1])
        elif cmd[0] == "pop_front":
            if dque:
                print(dque.popleft())
            else:
                print(-1)
        elif cmd[0] == "pop_back":
            if dque:
                print(dque.pop())
            else:
                print(-1)
        elif cmd[0] == "size":
            print(len(dque))
        elif cmd[0] == "empty":
            if dque:
                print(0)
            else:
                print(1)
        elif cmd[0] == "front":
            if dque:
                print(dque[0])
            else:
                print(-1)
        elif cmd[0] == "back":
            if dque:
                print(dque[-1])
            else:
                print(-1)

solution()