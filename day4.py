class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        gls=[[0.0 for _ in range(101)] for _ in range(101)]
        gls[0][0]=poured
        
        for i in range(query_row+1):
            for j in range(i+1):
                if gls[i][j]>1:
                    extra=gls[i][j]-1
                    gls[i][j]=1
                    gls[i+1][j]+=extra/2
                    gls[i+1][j+1]+=extra/2
        
        return gls[query_row][query_glass]          


# FASTER APPROACH

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        curr_row = [poured]
        for i in range(query_row):
            x = [0] + [ max(0, excess - 1) for excess in curr_row ] + [0]
            curr_row = [(x[i] + x[i + 1]) * 0.5 for i in range(len(x) - 1)]
        return min(curr_row[query_glass], 1)
