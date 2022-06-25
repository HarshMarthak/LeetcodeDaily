class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        pos = -1
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if pos != -1:
                    return False
                pos = i
        return pos in [-1,0,len(nums)-2] or nums[pos-1] <= nums[pos+1] or nums[pos] <= nums[pos+2]
