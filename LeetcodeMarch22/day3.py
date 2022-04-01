class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans=0
        count=0
        for i in range(2,len(nums)):
            if nums[i]-nums[i-1]==nums[i-1]-nums[i-2]:
                count+=1
                ans+=count
            else:
                count=0
        return ans