import sys
input = sys.stdin.readline

res = set()

n = int(input())
for _ in range(n):
    check = list(map(str, input().split()))
    if check[0] in res:
        res.remove(check[0])
    else:
        res.add(check[0])

print(*sorted(list(res), reverse=True))

# n = int(input())
# currMap = {}

# for _ in range(n):
#     name, state = map(str, input().split())
#     if state == "enter":
#         currMap[name] = 1
#     else:
#         del currMap[name]

# names = sorted(currMap.keys(), reverse=True)
# print(*names, sep="\n")