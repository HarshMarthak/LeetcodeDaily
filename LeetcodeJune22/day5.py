class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        posDiag = set() # r + c
        negDiag = set() # r - c
        res = 0
        def helper(r):
            nonlocal res
            if r == n:
                res += 1
                return

            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                helper(r + 1)

                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r- c)

        helper(0)
        return res
