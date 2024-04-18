import sys

num = int(input())
scoreArr = list(map(int, input().split()))
diffArr = [0 for _ in range(1 + num)]

for i in range(num + 1):
    maxNum = 0
    minNum = 10001
    for j in range(i, 0, -1):
        maxNum = max(maxNum, scoreArr[j-1])
        minNum = min(minNum, scoreArr[j-1])
        diffArr[i] = max(diffArr[i], maxNum - minNum + diffArr[j-1])

print(diffArr[num])