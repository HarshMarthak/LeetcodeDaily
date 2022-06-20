class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        temp=""
        words.sort(key=len,reverse=True)
        for word in words:
            word+="#"
            if not (word in temp):
                temp+=word
        return len(temp)

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key=lambda x: (x[::-1]), reverse=True)
        print(words)
        last = words[0]
        res = len(last)+1
        for w in words[1:]:

            if not last.endswith(w):
                res += len(w)+1
                last = w
        return res
