class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words: return []
        ans=[]
        window=len(words)*len(words[0])
        for i in range(0,len(s)-window+1):
            temp=s[i:i+window]
            exist=True
            for w in words:
                if w not in temp:
                    exist=False
                    break
            if exist:
                ans.append(i)
        return ans