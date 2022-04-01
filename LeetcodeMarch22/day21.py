class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans=[]
        last_index=[0 for _ in range(26)]
        length=len(s)
        for i in range(lenght):
            last_index[ord(s[i])-97]=i
        first=0
        last=0

        for i in range(lenght):
            last=max(last,last_index[ord(s[i])-97])
            if last==i:
                ans.append(last-first+1)
                first=i+1
        return ans


# better appraoch from discussion


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        rightmost = {c:i for i, c in enumerate(S)}
        left, right = 0, 0
    
        result = []
        for i, letter in enumerate(S):
    
            right = max(right,rightmost[letter])
        
            if i == right:
                result += [right-left + 1]
                left = i+1
    
        return result