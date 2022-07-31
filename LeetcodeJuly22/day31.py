class NumArray:
    def __init__(self, nums):
        self.nums = nums
        self.sums = sum(nums)

    def update(self, index, val):
        self.sums += val-self.nums[index]
        self.nums[index] = val

    def sumRange(self, left, right):
        return sum(self.nums[left:right+1]) if right-left < len(self.nums)//2 else self.sums - sum(self.nums[:left]) - sum(self.nums[right+1:])
