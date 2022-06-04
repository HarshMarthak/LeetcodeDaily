class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiagonals = set()
        negDiagonals = set()
        res = []
        board = [['.'] * n for i in range(n)]

        def backtrack(r = 0):
            if r == n:
                path = [''.join(row) for row in board]
                res.append(path)
                return

            for c in range(n):
                if c in col or r+c in posDiagonals or r-c in negDiagonals:
                    continue

                col.add(c)
                posDiagonals.add(r+c)
                negDiagonals.add(r-c)
                board[r][c] = 'Q'

                backtrack(r + 1)
                col.remove(c)
                posDiagonals.remove(r+c)
                negDiagonals.remove(r-c)
                board[r][c] = '.'

        backtrack()
        return res
