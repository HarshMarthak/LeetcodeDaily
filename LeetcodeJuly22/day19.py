class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        t = []
        for i in range(numRows):
            t.append([])
            for j in range(i + 1):
                if j == 0 or j == i:
                    t[i].append(1)
                else:
                    t[i].append(t[i - 1][j - 1] + t[i - 1][j])
        return t
