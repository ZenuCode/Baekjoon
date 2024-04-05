class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = sorted(nums1 + nums2)
        if len(arr) % 2 == 0:
            a = len(arr) // 2
            b = a - 1
            return ((arr[a] + arr[b]) / 2)
        else:
            m = len(arr) // 2
            return arr[m]