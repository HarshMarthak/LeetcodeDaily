#my solution
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        return nums
#faster solution
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s1 = 0
        l = []
        for i in range(len(nums)):
            s1 += nums[i]
            l.append(s1)
        return l
