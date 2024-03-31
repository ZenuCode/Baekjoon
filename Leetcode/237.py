class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix # This order -> [1, 1, 2, 6]
            prefix *= nums[i] # 1, 1, 2, 6
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix # [24, 12, 8, 6] <- This order
            postfix *= nums[i] # (1 * 24) <- (6 * 2) <- (2 * 4) <- (6 * 1)  
            # 4 * 1, 3 * 4, 2 * 12, 1 * 24
        
        return res