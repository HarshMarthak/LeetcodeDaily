class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = {}
        
        for num in nums:
            if num in d:
                return num
            else:
                d[num] = 0



#dicussion sol

class Solution:
    def findDuplicate(self, A):
        tort,hare = A[0],A[A[0]]
        while hare!=tort:
            tort,hare = A[tort],A[A[hare]]
        tort = 0
        while hare!=tort:
            tort,hare = A[tort],A[hare]
        return tort