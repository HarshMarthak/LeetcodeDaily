class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def findParent(v,parents):
            if v==parents[v]:
                return v
            parents[v]=findParent(parents[v],parents)
            return parents[v]
        parents=[i for i in range(26)]
        for eq in equations:
            if eq[1]=="=":
                U=findParent(ord(eq[0])-ord('z'),parents)
                V=findParent(ord(eq[3])-ord('z'),parents)
                parents[U]=V
        for eq in equations:
            if eq[1]=="!":
                U=findParent(ord(eq[0])-ord('z'),parents)
                V=findParent(ord(eq[3])-ord('z'),parents)
                if U==V:
                    return False
        return True
