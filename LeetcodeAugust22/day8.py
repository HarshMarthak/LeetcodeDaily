class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        a = []
        for num in nums:
            idx = bisect.bisect_left(a, num)
            if idx == len(a):
                a.append(num)
            else:
                a[idx] = num
        return len(a)