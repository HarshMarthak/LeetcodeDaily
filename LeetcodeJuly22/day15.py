class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            c = 1
            grid[i][j] = 0
            if i > 0 and grid[i-1][j] == 1:
                c += dfs(i-1, j)
            if i < m - 1 and grid[i+1][j] == 1:
                c += dfs(i+1, j)
            if j > 0 and grid[i][j-1] == 1:
                c += dfs(i, j-1)
            if j < n - 1 and grid[i][j+1] == 1:
                c += dfs(i, j+1)
            return c
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cur = dfs(i, j)
                    res = max(res, cur)
        return res
