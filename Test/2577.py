import sys
from collections import Counter
input = sys.stdin.readline

num = 1
for _ in range(3):
    num *= int(input())

arr = list(map(int, str(num)))
res = Counter(arr)

for i in range(10):
	print(res[i])
