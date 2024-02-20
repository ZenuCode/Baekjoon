import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    arr = list(map(int, input()))
    ans = []
    stack = []

    for i in range(n):
        while stack:
            if stack[-1][1] > arr[i]:
                ans.append(stack[-1][0] + 1)
                break
            else:
                stack.pop()
        if not stack:
            ans.append(0)
        stack.append([i, arr[i]])

    return " ".join(map(str, ans))

print(solution())