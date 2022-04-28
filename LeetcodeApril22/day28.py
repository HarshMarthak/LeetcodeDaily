from heapq import heappop, heappush
class Solution:
    def minimumEffortPath(self, heights):
        heap = [[0, 0, 0]]
        m, n = len(heights), len(heights[0])
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        seen = [[False] * n for _ in range(m)]
        while heap:
            diff, i, j = heappop(heap)
            if i == m - 1 and j == n - 1:
                return diff
            if seen[i][j]:
                continue
            seen[i][j] = True
            for dx, dy in dir:
                di = i + dx
                dj = j + dy
                if di < 0 or di >= m or dj < 0 or dj >= n or seen[di][dj]:
                    continue
                heappush(heap, (max(diff, abs(heights[i][j] - heights[di][dj])), di, dj))
