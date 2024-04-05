class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return -1

        l, r = 0, len(nums) - 1
        while l <= r:
            center = (l + r) // 2
            if target < nums[center]:
                r = center - 1
            elif target > nums[center]:
                l = center + 1
            else:
                return center
        return -1