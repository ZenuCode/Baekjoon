# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countArr = Counter(nums)
        return [num for num, _ in countArr.most_common(k)]