class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def longestCommonSubsequence(self, text1: str, text2: str) -> int:
            def findLIS(array):
                stacks = [array[0]]
                for num in array[1:]:
                    find_stack(stacks, num)
                return len(stacks)


            def find_stack(s,n):
                l = 0
                r = len(s)
                while l < r:
                    m = (l+r)//2
                    if s[m] < n:
                        l = m+1
                    else:
                        r = m
                if l == len(s):
                    s.append(n)
                else:
                    s[l] = n
            dp = defaultdict(deque)
            n, m = len(text1), len(text2)
            if n == 0 or m == 0:
                return 0
            if n < m:
                text1, text2 = text2, text1
            for index, char in enumerate(text1):
                dp[char].appendleft(index)
            arr = []
            for char in text2:
                if char in dp:
                    arr+=dp[char]
            if arr:
                return findLIS(arr)
            return 0
        n = longestCommonSubsequence(self,word1,word2)
        d1, d2 = len(word1)-n, len(word2)-n
        return d1+d2
