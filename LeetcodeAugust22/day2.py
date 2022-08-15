class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        a=[]
        for x in matrix:
            a.extend(x)
        a.sort()
        return a[k-1]