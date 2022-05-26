class Solution:
    def maxEnvelopes(self, l: List[List[int]]) -> int:
        if len(l)==1:
            return 1
        l.sort(key=lambda x:(x[0], -x[1]))
        size = 0
        dp = [0]*len(l)

        for _, h in l:
            l, r = 0, size-1
            while l <= r:
                mid = (l+r) // 2
                if dp[mid] >= h:
                    r = mid - 1
                else:
                    l = mid + 1

            dp[l] = h
            size = max(size, l+1)
        return size
