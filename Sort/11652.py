import sys
input = sys.stdin.readline

numMap = {}

for _ in range(int(input())):
    val = int(input())
    numMap[val] = numMap.get(val, 0) + 1

numMap = sorted(numMap.items(), key = lambda x : (-x[1], x[0]))
print(numMap[0][0])