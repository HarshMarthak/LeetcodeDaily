class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n, m = len(matrix), len(matrix[0])
        answer = 0

        for i in range(n):
            for j in range(1, m):
                matrix[i][j] += matrix[i][j - 1]

        for j in range(m):
            for k in range(j, m):
                d, c = {0: 1}, 0
                for i in range(n):
                    c += matrix[i][k] - (matrix[i][j - 1] if j else 0)
                    if c - target in d:
                        answer += d[c - target]
                    d[c] = d[c] + 1 if c in d else 1
        return answer
