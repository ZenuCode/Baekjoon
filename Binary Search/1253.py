import sys

n = int(sys.stdin.readline())
nums = sorted(list(map(int, sys.stdin.readline().split())))
count = 0

def binary_search(nums, idx):
    arr = nums.copy()
    target = arr.pop(idx)
    lp, rp = 0, len(arr) - 1
    while lp < rp:
        total = arr[lp] + arr[rp]
        if total > target:
            rp -= 1
        elif total < target:
            lp += 1
        else:
            return 1
    return 0

total = 0
for i in range(n):
    total += binary_search(nums, i)

print(total)