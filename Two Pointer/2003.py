import sys
input = sys.stdin.readline

n, target = map(int, input().split())
arr = list(map(int, input().split()))

l, r = 0, 0
currSum = 0
res = 0

while r <= len(arr):
    if currSum < target:
        if r < len(arr):
            currSum += arr[r]
        r += 1
    elif currSum > target:
        currSum -= arr[l]
        l += 1
    else:
        res += 1
        if r < len(arr):
            currSum += arr[r]
        r += 1

print(res)

"""

import sys
input = sys.stdin.readline

a,b = map(int, input().split())
nums = list(map(int, input().split()))


num = 0
answer = 0
start = 0
end = 0

while end<a:
    num += nums[end]
    end += 1
    while num>b:
        num -= nums[start]
        start+=1

    if num==b:
        answer += 1
print(answer)

"""