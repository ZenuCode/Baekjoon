import sys
input = sys.stdin.readline

stack = []

def backTrack(depth, index):
    if depth == 6:
        print(*stack)
        return
    
    for i in range(index, n):
        stack.append(arr[i])
        backTrack(depth + 1, i + 1)
        stack.pop()

while True:
    arr = list(map(int, input().split()))
    n = arr[0]
    arr = arr[1:]
    if n == 0:
        break
    backTrack(0, 0)
    print()

# from itertools import combinations

# while True:
#     arr = list(map(int, input().split()))
#     n = arr[0]
#     arr = arr[1:]
#     if n == 0:
#         break

#     for i in combinations(arr, 6):
#         for j in i:
#             print(j, end=' ')
#         print()
#     print()