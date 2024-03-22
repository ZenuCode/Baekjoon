import sys
input = sys.stdin.readline

arr = [input().rstrip() for _ in range(int(input()))]
arr = list(set(arr))
arr.sort()
arr.sort(key=len)

print(*arr, sep="\n")