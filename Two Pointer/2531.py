import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().rstrip().split())
sushi = [int(input()) for _ in range(n)]
res = 0
for i in range(n):
    if i+k > n:
        currMax = len(set(sushi[i:n] + sushi[:(i+k)%n] + [c]))
    else:
        currMax = len(set(sushi[i:i+k] + [c]))
    if res < currMax:
        res = currMax
print(res)