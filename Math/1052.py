import sys

n, k = map(int, sys.stdin.readline().split())
count = 0

while bin(n).count('1') > k:
    n = n + 1
    count = count + 1

print(count)