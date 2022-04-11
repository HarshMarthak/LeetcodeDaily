class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        temp=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                temp.append(grid[i][j])
        k=k%len(temp)
        temp=temp[-k:]+temp[:-k]
        k=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j]=temp[k]
                k+=1
        return grid
# advanced solution

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        k %= (m * n)
        flat = tuple(grid[i][j] for i in range(m) for j in range(n))
        flat = flat[-k:] + flat[:-k]
        ans = [[flat[i * n + j] for j in range(n)] for i in range(m)]
        return ans
