import time

def find_sub_array(arr: list[int], s: int) -> list[int]:
    left: int = 0
    sub_total: int = 0
    for right in range(len(arr)):
        sub_total += arr[right]
        while left < right and sub_total > s:
            sub_total -= arr[left]
            left += 1
        if sub_total == s:
            return [left+1, right+1]
    return [-1]


start_time = time.time()
print(find_sub_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15))
print(print("--- %s seconds ---" % (time.time() - start_time)))