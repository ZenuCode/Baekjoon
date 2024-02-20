import sys

n = int(input())

end: int = 0
max: int = 0

arr = []

for i in range(0,n):
    a, b = map(int,sys.stdin.readline().rstrip().split())
    arr.append([a,b])

arr.sort(key=lambda x: (x[1], x[0]))
print(arr)

for newStart, newEnd in arr:
    if end <= newStart:
        max += 1
        end = newEnd
print(max)