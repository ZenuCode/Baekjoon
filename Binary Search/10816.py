from sys import stdin

n = stdin.readline().rstrip()
card = list(map(int,stdin.readline().split()))
m = stdin.readline().rstrip()
test = list(map(int,stdin.readline().split()))

hash = {}

for i in card:
    if i in hash:
        hash[i] += 1
    else:
        hash[i] = 1

for i in test:
    if i in hash:
        print(hash[i], end=' ')
    else:
        print(0, end=' ')


# import sys
# n = sys.stdin.readline().rstrip()
# card = list(map(int, sys.stdin.readline().split()))
# m = sys.stdin.readline().rstrip()
# test = list(map(int, sys.stdin.readline().split()))

# card.sort()

# def binary_search(array, target, start, end):
#     if start > end:
#         return 0
#     mid = (start + end) // 2
#     if array[mid] == target:
#         return array[start:end+1].count(target)
#     elif array[mid] < target:
#         return binary_search(array, target, mid+1, end)
#     else:
#         return binary_search(array, target, start, mid-1)

# for i in range(len(test)):
#     print(binary_search(card, test[i], 0, len(card)-1), end=' ')