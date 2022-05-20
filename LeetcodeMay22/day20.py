#Brute force (TLE)

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        ROWS=len(obstacleGrid)
        COLS=len(obstacleGrid[0])
        totalPath=0
        def dfs(i,j):
            if i==ROWS or i<0 or j==COLS or j<0:
                return
            if obstacleGrid[i][j]==1:
                return
            if i==ROWS-1 and j==COLS-1:
                nonlocal totalPath
                totalPath+=1
            dfs(i+1,j)
            dfs(i,j+1)
            return
        dfs(0,0)
        return totalPath


#better solution using dynamic programming O(M*N)


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS,COLS=len(obstacleGrid),len(obstacleGrid[0])
        dp = [[0 for _ in range(COLS)] for _ in range(ROWS)]

        for i in range(COLS):
            if obstacleGrid[0][i] == 1:
                break
            dp[0][i] = 1
        for i in range(ROWS):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        for i in range(1,ROWS):
            for j in range(1,COLS):
                if obstacleGrid[i][j] ==1:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

#inplace solution using dp

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]==1 or obstacleGrid[-1][-1]==1:
            return 0
        ROWS,COLS=len(obstacleGrid),len(obstacleGrid[0])
        flag=1
        for i in range(COLS):
            if obstacleGrid[0][i] == 1:
                flag=0
            obstacleGrid[0][i] = flag
        flag=1
        for i in range(1,ROWS):
            if obstacleGrid[i][0] == 1:
                flag=0
            obstacleGrid[i][0] = flag
        for i in range(1,ROWS):
            for j in range(1,COLS):
                if obstacleGrid[i][j] ==1:
                    obstacleGrid[i][j]=0
                    continue
                obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        return obstacleGrid[-1][-1]
