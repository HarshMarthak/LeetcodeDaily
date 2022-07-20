class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        word_count = dict()
        for word in words:
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1
        count = 0
        for word in word_count:
            i = 0
            for char in word:
                i = s.find(char, i) + 1
                if not i:
                    break
            if i:
                count += word_count[word]
        return count
