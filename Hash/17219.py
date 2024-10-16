import sys
input = sys.stdin.readline

n, m = map(int, input().split())
webMap = {}
for _ in range(n):
    link, word = input().split()
    webMap[link] = word

for _ in range(m):
    link = input().strip()
    print(webMap[link])