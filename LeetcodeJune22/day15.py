class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # def isPredecessor(a,b):
        #     if (a in b) and len(a)+1==len(b):
        #         return True
        #     return False
        words.sort(key=lambda x:len(x))
        dp={}
        for i in range(len(words)):
            word=words[i]
            currMax=1
            for j in range(len(word)):
                temp=word[:j]+word[j+1:]
                if temp in dp:
                    currMax=max(currMax,dp[temp]+1)
            dp[word]=currMax
        return max(dp.values())
