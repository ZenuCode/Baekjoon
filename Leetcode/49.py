# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/description/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arrange = defaultdict(list) # sorted: [indexes]
        for s in strs:
            arrange["".join(sorted(s))].append(s) 
        return arrange.values()  