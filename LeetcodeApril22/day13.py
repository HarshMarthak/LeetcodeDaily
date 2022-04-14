class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans=[[0 for _ in range(n)] for _ in range(n)]
        x=y=dx=0
        dy=1
        for i in range(1,n*n):
            if dy==0 and (x + dx == n or ans[x + dx][y] != 0):
                dy=-1*dx
                dx=0
            elif dx==0 and (y + dy == n or y + dy == -1 or ans[x][y+dy]!=0):
                dx = dy
                dy = 0
            ans[x][y] = i
            
            x = x + dx
            y = y + dy
        return ans