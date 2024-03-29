# Two Sum
# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {} #val : index

        for i, n in enumerate(nums):
            diff = target - nums[i]
            if diff in values:
                return([values[diff], i])
            values[n] = i