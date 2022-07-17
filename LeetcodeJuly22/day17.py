#my solution
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        ds = [0] + [1] * (k + 1)
        for i in range(2, n+1):
            new = [0]
            for j in range(k+1):
                v = ds[j+1]
                v -= ds[j-i+1] if j >= i else 0
                new.append( (new[-1] + v) % MOD )
            ds = new
        return (ds[k+1] - ds[k]) % MOD

#faster solution

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:

        dp = [0] * (k + 1)
        dp[0] = 1

        dp_new = [0] * (k + 1)
        c = 2

        while c <= n:
            s = 0
            for i in range(k + 1):
                s += dp[i]
                if i - c >= 0:
                    s -= dp[i - c]

                s = s % (10 ** 9 + 7)
                dp_new[i] = s

            dp = dp_new
            dp_new = [0] * (k + 1)
            c += 1

        return dp[k]
