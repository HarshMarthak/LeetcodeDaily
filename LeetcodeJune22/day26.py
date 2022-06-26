#my solution

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        s = sum(cardPoints[:k])
        res = s
        for i in range(1, k+1):
            s += cardPoints[-i] - cardPoints[k-i]
            res = max(res, s)
        return res

#better solution

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len( cardPoints )
        totalPoints = sum( cardPoints )
        r = n - k
        if r == 0:
            return totalPoints
        Min = float('inf')

        lo, hi  = 0, r
        Sum = sum( cardPoints[lo:hi] )
        Min = Sum

        for i in range(0, n-r):
            valPop = cardPoints[lo]
            valAdd = cardPoints[hi]
            Sum += valAdd - valPop
            if Sum < Min:
                Min = Sum
            lo += 1
            hi += 1

        return totalPoints - Min


