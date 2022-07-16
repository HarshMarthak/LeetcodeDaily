#my solution

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        def solve(i, j, maxMove, mem):
            if (i, j, maxMove) in mem:
                return mem[(i, j, maxMove)]
            if maxMove < 0:
                return 0
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1

            up = solve(i - 1, j, maxMove - 1, mem)
            down = solve(i + 1, j, maxMove - 1, mem)
            left = solve(i, j - 1, maxMove - 1, mem)
            right = solve(i, j + 1, maxMove - 1, mem)

            mem[(i, j, maxMove)] = up + down + left + right
            return mem[(i, j, maxMove)]

        return solve(startRow, startColumn, maxMove, dict()) % 1000000007

#better solution

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @lru_cache(None)
        def moves(move,row,col):
            if row==m or row<0 or col<0 or col==n:
                return 1
            if move==0:
                return 0
            move-=1
            return (moves(move,row+1,col)+moves(move,row,col+1)+moves(move,row-1,col)+moves(move,row,col-1))%((10**9)+7)

        return moves(maxMove,startRow,startColumn)
