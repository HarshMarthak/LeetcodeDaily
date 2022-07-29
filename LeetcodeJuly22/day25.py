class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if((target not in nums)or(len(nums)==0)):
            return [-1,-1]
        else:
            l=[]
            l.append(nums.index(target))
            n=len(nums)
            nums=nums[::-1]
            k=nums.index(target)+1
            l.append(n-k)
        return l
