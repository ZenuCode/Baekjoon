import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
res = 0

for each in arr:
    if each == 1:
        continue

    for i in range(2, each + 1):
        if i == each:
            res += 1
        elif each % i == 0:
            break 
    
print(res)