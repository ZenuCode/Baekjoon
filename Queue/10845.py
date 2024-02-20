import sys

n = int(input())
que = []

for i in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push":
        que.append(cmd[1])
    elif cmd[0] == "pop":
        if que:
            print(que.pop(0))
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(que))
    elif cmd[0] == "empty":
        if que:
            print(0)
        else:
            print(1)
    elif cmd[0] == "front":
        if que:
            print(que[0])
        else:
            print(-1)
    elif cmd[0] == "back":
        if que:
            print(que[-1])
        else:
            print(-1)