import sys
input = sys.stdin.readline

def find_closest_sum(arr):
    n = len(arr)
    arr.sort()
    closest_sum = float("inf")
    result = []

    for i in range(n - 2):
        l, r = i + 1, n - 1
        while l < r:
            current_sum = arr[i] + arr[l] + arr[r]
            if abs(current_sum) < abs(closest_sum):
                closest_sum = current_sum
                result = [arr[i], arr[l], arr[r]]

            if current_sum < 0:
                l += 1
            elif current_sum > 0:
                r -= 1
            else:
                return result

    return result

n = int(input())
arr = list(map(int, input().split()))
result = find_closest_sum(arr)

print(*result)
