class Solution:
    def isBipartite(self, graph):
        n, colors = len(graph), {}
        def dfs(i, color):
            if i in colors:
                return colors[i] == color
            colors[i] = color
            for nei in graph[i]:
                if not dfs(nei, 1-color): return False
            return True
        for i in range(n):
            if i not in colors:
                if not dfs(i, 0): return False
        return True
