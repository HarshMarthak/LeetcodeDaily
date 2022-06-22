#cheaty solution
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]

#Quick Select Solution
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(l, r):
            ri = randint(l, r)
            nums[r], nums[ri] = nums[ri], nums[r]
            for i, v in enumerate(nums[l: r+1], l):
                if v >= nums[r]:
                    nums[l], nums[i] = nums[i], nums[l]
                    l += 1
            return l - 1

        l, r, k = 0, len(nums) - 1, k - 1
        while True:
            pos = partition(l, r)
            if pos < k:
                l = pos + 1
            elif pos > k:
                r = pos - 1
            else:
                return nums[pos]
