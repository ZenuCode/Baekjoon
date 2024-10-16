import sys
input = sys.stdin.readline

n, m = map(int, input().split())
groupMap = {}

for _ in range(n):
    group = input().strip()
    num = int(input())
    names = set()
    for _ in range(num):
        names.add(input().strip())
    groupMap[group] = names

for _ in range(m):
    name = input().strip()
    test = int(input())
    if test == 0:
        print(*sorted(groupMap[name]), sep="\n")
    else:
        for key, val in groupMap.items():
            if name in val:
                print(key)