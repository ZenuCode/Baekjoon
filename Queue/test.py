import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
keyArr = list(map(int, sys.stdin.readline().split()))
queArr = deque([i for i in range(1, n + 1)])
count = 0

for key in keyArr:
    while 1:
        if queArr[0] == key:
            queArr.popleft()
            break
        else:
            if queArr.index(key) > len(queArr) // 2:
                while queArr[0] != key:
                    queArr.rotate(1)
                    count += 1
            else:
                while queArr[0] != key:
                    queArr.rotate(-1)
                    count += 1

print(count)