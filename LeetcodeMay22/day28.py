#first solution
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)+1):
            if i not in nums:
                return i
#better solution
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return int((len(nums) *(len(nums) + 1)/2) - sum(nums))
