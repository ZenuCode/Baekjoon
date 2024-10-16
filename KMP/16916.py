import sys
input = sys.stdin.readline

word = input().rstrip()
key = input().rstrip()

if key in word:
    print(1)
else:
    print(0)