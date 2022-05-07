class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack=[]
        minimum=-1000000001
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<minimum:
                return True
            while stack and stack[-1]<nums[i]:
                minimum=stack.pop()
            stack.append(nums[i])
        return False
