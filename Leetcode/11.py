class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = min(height[l], height[r]) * (r - l)
        while l < r:
            if height[l] < height[r]:
                l += 1
                ans = max(ans, min(height[l], height[r]) * (r - l))
            else:
                r -= 1
                ans = max(ans, min(height[l], height[r]) * (r - l))
        
        return(ans)
        