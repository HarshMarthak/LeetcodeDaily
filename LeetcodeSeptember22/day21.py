class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        temp=sum(num for num in nums if num%2==0)
        ans=[0]*len(queries)
        i=0
        for val,index in queries:
            if nums[index]%2==0:
                temp-=nums[index]
            nums[index]+=val
            if nums[index]%2==0:
                temp+=nums[index]
            ans[i]=temp
            i+=1
        return ans
