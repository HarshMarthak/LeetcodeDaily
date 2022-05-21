#simple dp solution
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[(amount+1) for _ in range(amount+1)]
        dp[0]=0

        for i in range(1,amount+1):
            for coin in coins:
                if i-coin >= 0:
                    dp[i]=min(dp[i],1+dp[i-coin])
        return dp[amount] if dp[amount]!=amount+1 else -1

#mathematical solution ఠ_ఠ

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        count, prev = 0, 1 << amount

        while prev & 1 == 0:
            curr = prev
            for coin in coins:
                curr |= prev >> coin

            if curr == prev:
                return -1

            count += 1
            prev = curr

        return count
