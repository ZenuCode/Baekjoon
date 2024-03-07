# import sys

# n = int(input())
# arr = list(map(int, sys.stdin.readline().rsplit()))
# arr.sort()
# key = int(input())
# count = 0
# i = 0
# j = n - 1

# while i < j:
#     res = arr[i] + arr[j]
#     if (res < key):
#         i += 1
#     elif(res > key):
#         j -= 1
#     else:
#         count += 1
#         i += 1
#         j -= 1

# print(count)

n = int(input())
arr = set(map(int, input().split()))
print(arr)
x = int(input())
cnt = 0
for num in arr:
    if x - num in arr:
        cnt += 1

print(cnt//2)