class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(h)
        verticalCuts.append(w)
        horizontalCuts.sort()
        verticalCuts.sort()
        maxh=horizontalCuts[0]
        maxw=verticalCuts[0]
        for i in range(1,len(horizontalCuts)):
            maxh=max(horizontalCuts[i]-horizontalCuts[i-1],maxh)
        for i in range(1,len(verticalCuts)):
            maxw=max(verticalCuts[i]-verticalCuts[i-1],maxw)
        return (maxw*maxh)%1000000007
