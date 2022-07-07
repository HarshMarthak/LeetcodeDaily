#my solution

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        ans=1
        chk=None
        for i in range (1,len(nums)):
            if nums[i]>nums[i-1] and chk != True:
                chk=True
                ans+=1
            if nums[i]<nums[i-1] and chk != False:
                chk=False
                ans+=1
        return ans

#other solution

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up = 1
        down = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 0:
                up = down + 1
            elif nums[i] - nums[i-1] < 0:
                down = up + 1
        return max(down, up)
