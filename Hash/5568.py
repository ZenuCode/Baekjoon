from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

cardArr = [input().rstrip() for _ in range(n)]
res = set()

for j in permutations(cardArr, k):
    res.add(''.join(j))
   
print(len(res))