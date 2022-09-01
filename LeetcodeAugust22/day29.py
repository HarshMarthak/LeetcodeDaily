class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        nc = len(grid[0])
        
        def dfs(r, c):
            grid[r][c] = '0'
            if r - 1 >= 0 and grid[r - 1][c] == '1': dfs(r - 1, c) 
            if r + 1 < nr and grid[r + 1][c] == '1': dfs(r + 1, c) 
            if c - 1 >= 0 and grid[r][c - 1] == '1': dfs(r, c - 1) 
            if c + 1 < nc and grid[r][c + 1] == '1': dfs(r, c + 1)
        
        numOfIslands = 0
        for i in range(0, nr):
            for j in range(0, nc):
                if grid[i][j] == '1':
                    numOfIslands += 1
                    dfs(i, j)
        return numOfIslands
