#my basic dp solution

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        L = len(strs)
        dp = [[0] * (n+1) for _ in range(m+1)]
        c = [(c['0'], c['1']) for c in map(Counter,strs)]
        for c0, c1 in c:
            for j in range(m+1)[::-1]:
                for k in range(n+1)[::-1]:
                    if j >= c0 and k >= c1:
                        dp[j][k] = max(dp[j][k], dp[j-c0][k-c1] + 1)
        return dp[m][n]

#faster better solution

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counter = Counter([(s.count('0'), s.count('1')) for s in strs])
        d = defaultdict(lambda: -1)

        def dfs(m, n, count):
            if d[(m, n)] >= count: return d[(m, n)]
            max_count = count
            d[(m, n)] = count

            for k, v in counter.items():
                if v <= 0: continue
                zeros, ones = k[0], k[1]
                if zeros <= m and ones <= n:
                    counter[k] -= 1
                    max_count = max(max_count, dfs(m - zeros, n - ones, count + 1))
                    counter[k] += 1
            return max_count
        result = dfs(m, n, 0)
        return result
