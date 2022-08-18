# O(nlogn)

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d={}
        for ele in arr:
            if ele not in d:
                d[ele]=0
            d[ele]+=1
        a=[d[i] for i in d]
        a.sort(reverse=True)
        count=ans=0
        for i in a:
            count+=i
            ans+=1
            if count>=len(arr)//2:
                return ans

# O(n)

from heapq import heappush, heappop

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d={}
        for ele in arr:
            if ele not in d:
                d[ele]=0
            d[ele]+=1
        temp=[]
        for i in d:
            heappush(temp,-d[i])
        ans=count=0
        while temp:
            ans+=1
            count-=heappop(temp)
            if count>=len(arr)//2:
                return ans
