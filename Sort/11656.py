import sys

string = sys.stdin.readline().rstrip()
arr = []

for i in range(len(string)):
    arr.append(string[i:])

print(*sorted(arr), sep="\n")