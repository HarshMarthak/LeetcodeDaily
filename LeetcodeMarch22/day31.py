class Solution:

    def isSplitPossible(self,nums,mid,m):
        totalSplit=currSum=0
        for num in nums:
            if currSum+num <=mid:
                currSum+=num
            else:
                currSum=num
                totalSplit+=1
        return totalSplit+1 <=m



    def splitArray(self, nums: List[int], m: int) -> int:
        maxNums,maxSum=max(nums),sum(nums)

        while maxNums<=maxSum:

            mid=maxNums+(maxSum - maxNums)//2

            if self.isSplitPossible(nums,mid,m):
                maxSum=mid-1
            else:
                maxNums=mid+1

        return maxNums