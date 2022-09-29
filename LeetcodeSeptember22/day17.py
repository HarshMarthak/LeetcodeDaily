class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        result = []
        ws = []
        for i, word in enumerate(words):
            ws.append((word,       False, i, len(word)))
            ws.append((word[::-1], True,  i, len(word)))
        ws.sort()
        for i, (a, a_reversed, a_idx, a_len) in enumerate(ws):
            for j in range(i + 1, len(ws)):
                b, b_reversed, b_idx, _ = ws[j]
                if b.startswith(a):
                    if a_idx != b_idx and a_reversed != b_reversed:
                        rest = b[a_len:]
                        if rest == rest[::-1]:
                            result.append([a_idx, b_idx] if b_reversed else [b_idx, a_idx])
                else:
                    break
        return result
