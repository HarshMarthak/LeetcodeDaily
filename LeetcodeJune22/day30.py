class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median=nums[len(nums)//2]
        ans=0
        for i in nums:
            ans+=abs(i-median)
        return ans
