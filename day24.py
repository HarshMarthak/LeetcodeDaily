class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans=low=0
        high=len(people)-1
        
        while low<=high:
            if people[low]+people[high]<=limit:
                low+=1
            high-=1
            ans+=1
        return ans