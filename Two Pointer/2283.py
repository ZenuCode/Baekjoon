import sys
input = sys.stdin.readline

n, k = map(int, input().split())
countArr = [0] * 1000002

for _ in range(n):
    start, end = map(int, input().split())
    countArr[start + 1] += 1
    countArr[end + 1] -= 1

for i in range(1, len(countArr)):
    countArr[i] += countArr[i-1]

l, r, sum = 0, 0, 0
flag = False

while l < 1000001 and r < 1000001:
    if sum == k:
        flag = True
        break
    if sum < k:
        r += 1
        sum += countArr[r]
    else:
        l += 1
        sum -= countArr[l]

if flag:
    print(l, r)
else:
    print(0, 0)
    