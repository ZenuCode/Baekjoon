from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

def sol(arr):
    answer = 0
    for i in range(len(arr)-2):
        left, right = i+1, N-1
        while left < right:
            result = arr[i]+arr[left]+arr[right]
            if result > 0:
                right -= 1
            else:
                if result == 0:
                    if arr[left] == arr[right]:
                        answer += right - left
                    else:
                        idx = bisect_left(arr, arr[right])
                        answer += right-idx+1
                left += 1
    return answer

print(sol(arr))


# from sys import stdin
# # 이분탐색

# n = int(stdin.readline())
# arr = list(map(int, stdin.readline().split()))
# arr.sort()
# ans = 0


# def solve(s, e, g):
#     global ans
#     max_idx = n
#     while s < e:
#         tmp = arr[s] + arr[e]
#         if tmp < goal:
#             s += 1

#         elif tmp == g:
#             if arr[s] == arr[e]:
#                 ans += e - s

#             else:
#                 if max_idx > e:
#                     max_idx = e
#                     while max_idx >= 0 and arr[max_idx - 1] == arr[e]:
#                         max_idx -= 1
#                 ans += e - max_idx + 1
#             s += 1
#         else:
#             e -= 1


# for i in range(n - 2):
#     start = i + 1
#     end = n - 1
#     goal = -arr[i]
#     solve(start, end, goal)

# print(ans)