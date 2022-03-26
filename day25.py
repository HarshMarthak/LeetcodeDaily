class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n=len(costs)
        costDifference=[0 for _ in range(n)]
        totalCity_A_Cost=0
        for i in range(n):
            totalCity_A_Cost +=costs[i][0]
            costDifference[i]=costs[i][1]-costs[i][0]
        costDifference.sort()
        
        for i in range(n//2):
            totalCity_A_Cost += costDifference[i]
        
        return totalCity_A_Cost