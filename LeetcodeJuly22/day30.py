class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        words2freq, ans, cmax = {}, [], 0
        for word in words2:
            for char in word:
                count = word.count(char)
                if char in words2freq:
                    diff = count - words2freq[char]
                    if diff > 0:
                        words2freq[char] = count
                        cmax += diff
                else:
                    words2freq[char] = count
                    cmax += count
            if cmax > 10:
                return ans
        for word in words1:
            if len(word) < cmax:
                continue
            for char in words2freq:
                if word.count(char) < words2freq[char]:
                    break
            else:
                ans.append(word)
        return ans
