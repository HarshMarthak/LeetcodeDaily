class Solution:
    def maximumScore(self, nums: List[int], m: List[int]) -> int:
        p, n = len(m), len(nums)
        remain = n - p
        dp = [0] * (p + 1)
        for i in range(p):
            mm = m[-i - 1]
            for j in range(p - i):
                dp[j] = max(mm * nums[j] + dp[j + 1], mm * nums[j + remain] + dp[j])
            remain += 1
        return dp[0]
