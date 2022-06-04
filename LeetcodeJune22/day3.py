#my solution
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix: return
        m, n = len(matrix), len(matrix[0])
        dp = self.dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] + matrix[i][j] - dp[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        dp = self.dp
        return dp[row2+1][col2+1] - dp[row2+1][col1] - dp[row1][col2+1] + dp[row1][col1]

#faster solution
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m,n = len(matrix), len(matrix[0])
        self.acc = [[0]*n for _ in range(m)]
        for row in range(m):
            rowSum = 0
            for col in range(n):
                upperRectSum = 0 if row == 0 else self.acc[row-1][col]
                rowSum += matrix[row][col]
                self.acc[row][col] = rowSum + upperRectSum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        upperRect = 0 if row1 == 0 else self.acc[row1-1][col2]
        leftRect = 0 if col1 == 0 else self.acc[row2][col1-1]
        diagRect = 0 if col1==0 or row1==0 else self.acc[row1-1][col1-1]
        return self.acc[row2][col2]-upperRect-leftRect+diagRect
