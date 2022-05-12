#my solution 41% time 96% space
class Solution:
    def permuteUnique(self, nums):
        ans = [[]]
        for n in nums:
            temp = []
            for l in ans:
                for i in range(len(l)+1):
                    temp.append(l[:i]+[n]+l[i:])
                    if i<len(l) and l[i]==n: break
            ans = temp
        return ans

#other solution 99% time 47% space
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def rotate(nums, l):
            tmp = nums[l]
            i = l + 1
            while i < n:
                nums[i-1] = nums[i]
                i += 1
            nums[-1] = tmp
        def dfs(nums, l):
            if l == n-1:
                res.append(list(nums))
                return
            for i in range(l, n):
                if i > l and nums[i] == nums[l]: continue
                nums[l], nums[i] = nums[i], nums[l]
                dfs(nums, l+1)
            rotate(nums, l)
        nums.sort()
        dfs(nums, 0)
        return res


