from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # construct a BFS tree rooted at the pacific ocean and record what nodes we can reach
        # construct a BFS tree rooted at the atlantic ocean and record what nodes we can reach

        m = len(heights)
        n = len(heights[0])

        
        def BFS(grid, startingNodes):
            # return a list of reachable cells
            nonlocal m,n
            
            Q = deque()
            Q.extend(startingNodes)
            visited = set(startingNodes)
            while Q:
                r,c = Q.popleft()
                h = grid[r][c]
                
                # north
                if r>0 and grid[r-1][c]>=h and (r-1,c) not in visited:
                    visited.add((r-1,c))
                    Q.append((r-1,c))
                    
                # south
                if r<m-1 and grid[r+1][c]>=h and (r+1,c) not in visited:
                    visited.add((r+1,c))
                    Q.append((r+1,c))
                    
                # east
                if c>0 and grid[r][c-1]>=h and (r,c-1) not in visited:
                    visited.add((r,c-1))
                    Q.append((r,c-1))

                # east
                if c<n-1 and grid[r][c+1]>=h and (r,c+1) not in visited:
                    visited.add((r,c+1))
                    Q.append((r,c+1))
                    
            return visited
        
        
        pacificNeighbours = [(0,0)]
        for i in range(1,n):
            pacificNeighbours.append((0,i))
        for i in range(1,m):
            pacificNeighbours.append((i,0))

        atlanticNeighbours = [(m-1,n-1)]
        for i in range(n-1):
            atlanticNeighbours.append((m-1,i))
        for i in range(m-1):
            atlanticNeighbours.append((i,n-1))
            
        pCells = BFS(heights, pacificNeighbours)
        aCells = BFS(heights, atlanticNeighbours)
        
        X = pCells.intersection(aCells)
        return list(X)
