import sys
input = sys.stdin.readline

k, l = map(int, input().split())
classMap = {}
for i in range(l):
    student = input().strip()
    if student in classMap:
        del classMap[student]
    classMap[student] = i

print(*list(classMap.keys())[0:k], sep="\n")