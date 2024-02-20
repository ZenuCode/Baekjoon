import sys

testNum = int(input())

resultArr = []
max = 0

for i in range(0, testNum):
    batchNum = int(input())
    partArr = []
    result = 1
    for j in range(0, batchNum):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        partArr.append([a,b])

    partArr.sort(key=lambda x: (x[0]))
    max = partArr[0][1]

    for k in range(1, len(partArr)):
        if partArr[k][1] < max:
            result += 1
            max = partArr[k][1]
    resultArr.append(result)

for i in range(0, len(resultArr)):
    print(resultArr[i])