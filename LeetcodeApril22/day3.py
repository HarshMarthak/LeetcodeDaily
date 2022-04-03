class Solution:
    
    def nextPermutation(self, nums: List[int]) -> None:
        nums=self.nextP(nums)
        
        
        
    def nextP(self,nums):
        bp = len(nums)-2                    #breaking point
        ls = -1                       #lowest swap
        while bp>-1:
            if nums[bp] < nums[bp+1]:
                break
            bp-=1
        if bp < 0:
            nums.reverse()
        else:
            for ls in range(len(nums)-1,bp,-1):
                if nums[ls] > nums[bp]:
                    break
            nums[ls],nums[bp]=nums[bp],nums[ls]
            nums[bp+1:len(nums)]=nums[bp+1:len(nums)][::-1]
        return nums