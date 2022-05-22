#very low space solution

class Solution:
    def countSubstrings(self, s: str) -> int:
        return sum(s[i:j] == s[i:j][::-1] for j in range(len(s) + 1) for i in range(j))

#very fast runtime solution

class Solution:
    def countSubstrings(self, s: str) -> int:
        l, r = 0, 0
        num_palindromes = 0
        while r < len(s):
            while r<len(s) and s[r] == s[l]:
                r+=1
            num_palindromes += ((r-l)*(r-l+1))//2
            j = l-1
            k = r
            while j>=0 and k<len(s) and s[j]==s[k]:
                num_palindromes+=1
                j-=1
                k+=1
            l = r
        return num_palindromes
