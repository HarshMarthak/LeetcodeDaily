class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l=len(nums)
        j=0
        for i in range(l):
            if nums[i]%2==0:
                nums[j],nums[i]=nums[i],nums[j]
                j+=1
        return nums