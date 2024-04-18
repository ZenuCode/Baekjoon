import sys

testNum = int(input())
arr = []

for i in range(testNum):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    arr.append((a,1))
    arr.append((b,-1))

arr.sort()
total = 0
count = 0

for a, b in arr:
    count += b
    total = max(total, count)
print(total)