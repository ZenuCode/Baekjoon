import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
res = []

# Better way was to do A - B -> Automatically only leaves A individal
for each in A:
    if each not in B:
        res.append(each)

total = len(res)
print(total)
if total: print(*sorted(res))