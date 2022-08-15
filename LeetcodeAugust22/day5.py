class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums or target <= 0:
            return 0
        ans = 0
        memo = dict()
        def bt(rem):
            if rem == 0:
                return 1
            if rem in memo:
                return memo[rem]
            count = 0
            for num in nums:
                if num <= rem:
                    this_count = bt(rem-num)
                    count += this_count
            memo[rem] = count
            return count
        return bt(target)