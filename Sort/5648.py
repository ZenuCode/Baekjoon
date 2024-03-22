import sys
input = sys.stdin.read

n, *arr = input().split()
for i in range(int(n)):
    arr[i] = arr[i][::-1]
arr = list(map(int, arr))
print(*sorted(arr), sep="\n")