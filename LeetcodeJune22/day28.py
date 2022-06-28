#first Solution

class Solution:
    def minDeletions(self, s: str) -> int:
        l=[0 for _ in range(26)]
        for i in s:
            l[ord(i)-97]+=1
        l.sort(reverse=True)
        while l[-1]==0:
            l.pop()
        ans=0
        for i in range(1,len(l)):
            if l[i-1]==0:
                ans+=l[i]
                l[i]=0
                continue
            if l[i]>=l[i-1]:
                ans+=(l[i]-l[i-1])+1
                l[i]-=(l[i]-l[i-1]+1)
            print(l,ans)
        return ans

#second solution (better)

class Solution:
    def minDeletions(self, s: str) -> int:
        freq = {k: s.count(k) for k in 'abcdefghijklmnopqrstuvwxyz'}
        freq = dict(x for x in sorted(freq.items(), reverse=True, key=lambda item: item[1]) if x[1])
        print(freq)
        seen = set()
        ops = 0
        for key, value in freq.items():
            if value in seen:
                while value in seen:
                    ops += 1
                    value -= 1
            if value:
                seen.add(value)
        return ops
