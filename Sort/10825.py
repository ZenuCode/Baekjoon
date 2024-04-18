import sys
input = sys.stdin.readline

arr = []
for _ in range(int(input())):
    name, one, two, three = input().split()
    arr.append((-int(one), int(two), -int(three), name))

arr = sorted(arr)

for each in arr:
    print(each[3])