#my solution

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_hash = set(nums)
        ans = 0
        for num in nums:
            if num+1 in nums_hash:
                continue
            count = 0
            while num in nums_hash:
                count += 1
                num = num - 1
            ans = max(ans,count)
        return ans
