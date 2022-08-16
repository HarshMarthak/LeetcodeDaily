#my solution

class Solution:
    def firstUniqChar(self, s: str) -> int:
        arr = [0]*26
        for i in range(len(s)):
            arr[ord(s[i]) - ord('a')] += 1
        for i in range(len(s)):
            if arr[ord(s[i]) - ord('a')] == 1:
                return i
        return -1

#better solution

class Solution:
    def firstUniqChar(self, s: str) -> int:
        abc = "abcdefghijklmnopqrstuvwxyz"
        ans = 10**5
        for c in abc:
            idx = s.find(c);
            if (idx != -1 and idx == s.rfind(c)):
                ans = min(ans, idx)
        return ans if ans < 10**5 else -1
