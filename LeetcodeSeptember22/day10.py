class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0

        buy = [float(inf)]*k
        profit = [0]*k

        for p in prices:
            buy[0] = min(buy[0], p)
            profit[0] = max(profit[0], p - buy[0])
            for i in range(1,k):
                buy[i] = min(buy[i], p - profit[i-1])
                profit[i] = max(profit[i], p - buy[i])

        return profit[-1]
