class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        sl = len(stamp)
        out = []
        def singleStamp(t, left, right, offset):
            if t == "":
                return True
            idx = t.find(stamp)
            if idx >= 0:
                out.append(idx + offset)
                return singleStamp(t[:idx], left, True, offset) and singleStamp(t[idx+sl:], True, right, offset+idx+sl)
            if not left and not right:
                return False
            if left:
                for i in range(1,sl + 1):
                    if t[:i] == stamp[-i:]:
                        out.append(i + offset - sl)
                        return singleStamp(t[i:], True, right, offset+i)
            if right:
                for i in range(1,sl + 1):
                    if t[-i:] == stamp[:i]:
                        out.append(-i + len(t) + offset)
                        return singleStamp(t[:-i], left, True, offset)
            if not (left and right):
                return False
            idx = stamp.find(t)
            if idx >= 0:
                out.append(-idx + offset)
                return True
            return False
        
        if singleStamp(target, False, False, 0):
            out.reverse()
            return out
        return []
