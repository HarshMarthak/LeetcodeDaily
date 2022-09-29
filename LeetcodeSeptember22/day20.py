class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        nums2_str = "".join([chr(x) for x in nums2])
        nums1_str = "".join([chr(x) for x in nums1])
        N = len(nums1_str)
        res = 0
        i = 0
        for j in range(1, N+1):
            if nums1_str[i:j] in nums2_str:
                res = max(res, j-i)
            elif i < j:
                i += 1
        
        return res
