class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        seen = {}
        def dfs(p1, p2):
            p3 = p1 + p2
            if p3 == len(s3):
                return True
            if (p1, p2) in seen:
                return seen[(p1, p2)]
            val = False
            if p1 < len(s1):
                if s1[p1] == s3[p3]:
                    val = val or dfs(p1+1, p2)
            if p2 < len(s2):
                if s2[p2] == s3[p3]:
                    val = val or dfs(p1, p2+1)
            seen[(p1, p2)] = val
            return val
        return dfs(0,0)
