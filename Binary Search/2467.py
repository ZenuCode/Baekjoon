import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

def solve():
    l, r = 0, len(arr) - 1
    res = [1e10, 1e10]

    while l < r:
        check = arr[l] + arr[r]
        if check == 0:
            res = [arr[l], arr[r]]
            break
        elif abs(check) <= abs(res[0] + res[1]):
            res = [arr[l], arr[r]]

        if check < 0:
            l += 1
        else:
            r -= 1
    
    print(*res)

solve()