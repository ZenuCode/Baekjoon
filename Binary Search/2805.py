import sys

n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

start, end = 1, max(lst) 

while start <= end:
    sum = 0
    mid = (start + end) // 2  

    for l in lst:
        if l > mid:
            sum += l - mid
    
    if sum < m:  
        end = mid - 1  
    else:  
        start = mid + 1

# print(end)

# import sys
# from collections import Counter

# n, m = map(int, sys.stdin.readline().split())
# trees = Counter(map(int, sys.stdin.read().split()))

# s = 1
# e = 1000000000

# while s <= e:
#     mid = (s + e) // 2 
#     tot = sum((h - mid) * i for h, i in trees.items() if h > mid)

#     if tot >= m:
#         s = mid + 1
#     elif tot < m:
#         e = mid - 1

# print(e)