#my solution
class Solution:
    def countVowelStrings(self,n):
        return int((n+1)*(n+2)*(n+3)*(n+4)/24)


#dp solution
class Solution:
    def countVowelStrings(self,n):
        dp = [[1] * 6] + [[0] * 6 for i in range(n)]
        for i in range(1, n + 1):
            for k in range(1, 6):
                dp[i][k] = dp[i][k - 1] + dp[i - 1][k]
        return dp[n][5]
