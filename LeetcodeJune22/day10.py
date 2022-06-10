class Solution:
    def lengthOfLongestSubstring(self, s):
        dicts = {}
        maxlength = start = 0
        for i,value in enumerate(s):
            if value in dicts:
                sums = dicts[value] + 1
                if sums > start:
                    start = sums
            num = i - start + 1
            if num > maxlength:
                maxlength = num
            dicts[value] = i
        return maxlength


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        if len(s) == 2:
            return 1 if s[0] == s[1] else 2
        start = largest = l = i = 0
        store: {str, int} = {}
        for i in range(0, len(s)):
            c = s[i]
            if (c in store) and  (store[c] >= start):
                l = i - start
                if l > largest:
                    largest = l
                start = store[c]+1
            store[c] = i
        return max((i+1)-start, largest)
