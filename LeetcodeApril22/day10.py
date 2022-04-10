class Solution:
    def calPoints(self, ops: List[str]) -> int:
        l=[]
        for i in ops:
            if i=='+':
                l.append(l[-1]+l[-2])
            elif i=='D':
                l.append(2*l[-1])
            elif i=='C':
                l.pop()
            else:
                l.append(int(i))
        return sum(l)