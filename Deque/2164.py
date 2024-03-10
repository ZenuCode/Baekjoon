import sys
from collections import deque
input = sys.stdin.readline
cardArr = deque([i for i in range(1, int(input()) + 1)])

while len(cardArr) != 1:
    cardArr.popleft()
    cardArr.append(cardArr.popleft())

print(cardArr[0])