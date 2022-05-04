#my approach
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        frqMap=defaultdict(int)
        ans=0
        for i in nums:
            if frqMap[k-i]>0:
                ans+=1
                frqMap[k-i]-=1
            else:
                frqMap[i]+=1
        return ans

#another approach
from collections import Counter
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        ans = 0
        for c in counter:
            o = k-c
            if c<o:
                ans += min(counter[c],counter[o])
            elif c==o:
                ans += counter[c]//2
        return ans
