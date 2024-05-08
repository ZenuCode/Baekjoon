import sys
input = sys.stdin.readline

n, target = int(input().split())

price = [int(input()) for _ in range(n)]

print(price)