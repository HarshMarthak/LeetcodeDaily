class Solution:
    def validPalindrome(self, s):
        i, j = 0, len(s) - 1
        
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return self.validPalindromeUtil(s, i + 1, j) or self.validPalindromeUtil(s, i, j - 1)
        return True
    
    def validPalindromeUtil(self, s, i, j):
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        
        return True
                

# Alternate Solution

class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0 
        j = len(s) - 1
        if s == s[::-1]:
            return True
        
        while i < j: 
            if s[i] == s[j]: 
                i += 1
                j -= 1
            else: 
                s_skip_i = s[:i] + s[i+1:]
                s_skip_j = s[:j] + s[j+1:]
                if s_skip_i == s_skip_i[::-1] or s_skip_j == s_skip_j[::-1]:
                    return True 
                return False                 
        
        return False 