class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        l1=[]
        l2=[]
        for i in range(len(s)):
            if l1 and s[i]=="#":
                l1.pop()
            elif s[i]!="#":
                l1.append(s[i])
        for i in range(len(t)):
            if l2 and t[i]=="#":
                l2.pop()
            elif t[i]!="#":
                l2.append(t[i])
        return l1==l2