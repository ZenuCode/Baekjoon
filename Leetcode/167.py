class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        
        while l < r:
            sum_val = numbers[l] + numbers[r]
            if sum_val > target:
                r -= 1
            elif sum_val < target:
                l += 1
            else:
                return [l + 1, r + 1]
        """
        numSet = {}
        for i, n in enumerate(numbers):
            diff = target - n
            if diff in numSet:
                return [numSet[diff] + 1, i + 1]
            numSet[n] = i
        """
        