#dp solution

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid=[[1 for _ in range(n)] for j in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j]=grid[i-1][j]+grid[i][j-1]
        return grid[-1][-1]

#space optimized dp

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid=[1 for _ in range(n)]
        for _ in range(m-1):
            for j in range(1,n):
                grid[j]+=grid[j-1]
        return grid[-1]

#math solution

class Solution:
    def uniquePaths(self, m, n):
        return factorial(m+n-2) // factorial(m-1) // factorial(n-1)
