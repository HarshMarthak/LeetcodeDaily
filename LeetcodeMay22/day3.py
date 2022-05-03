class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start=end=-1
        temp=0
        for i in range(len(nums)):
            if nums[i]<nums[temp]:
                end=i
            else:
                temp=i
        temp=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if nums[i]>nums[temp]:
                start=i
            else:
                temp=i
        if start==end:
            return 0
        return end-start+1