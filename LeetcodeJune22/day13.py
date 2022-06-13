class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        if not triangle: return
        row = triangle[-1]
        for i in range(len(triangle)-2, -1,-1):
            for j in range(len(triangle[i])):
                row[j] = min(row[j], row[j+1]) + triangle[i][j]

        return row[0]
