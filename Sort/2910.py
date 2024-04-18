import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = map(int, input().split())
numMap = {}
index = 1

for num in arr:
    if num in numMap:
        numMap[num][0] += 1
    else:
        numMap[num] = [1, index]
        index += 1

numbers = [[i, j] for i, j in numMap.items()]
numbers.sort(key = lambda x : (-x[1][0], x[1][1]))
ans = []
for i, j in numbers:
    ans += [i] * j[0]

print(*ans)