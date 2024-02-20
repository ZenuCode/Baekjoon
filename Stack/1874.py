import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    cur = 1
    stack = []
    ans = []

    for i in range(n):
        val = int(input())
        while cur <= val:
            stack.append(cur)
            ans.append("+")
            cur += 1
        if val != stack.pop():
            return("NO")
        ans.append("-")
    return '\n'.join(ans)

print(solution())