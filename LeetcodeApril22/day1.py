class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s)-1
        
        while(j >= i):
            s[i], s[j] = s[j], s[i]
            i = i+1
            j = j-1






class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)//2): s[i], s[~i] = s[~i], s[i]