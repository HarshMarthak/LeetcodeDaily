class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        count = 0
        for i, ch in enumerate(s):
            if ch == '(':
                count += 1
            elif ch == ')':
                count -= 1

            if count < 0: 
                
                s[i] = ''
                count += 1
           

        if count > 0:
            
            for i in range(len(s)-1, -1, -1):
                if s[i] == '(': 
                    s[i] = ''
                    count -= 1
                if count == 0: break
            
        return ''.join(s)