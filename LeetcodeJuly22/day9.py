#my solution

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dq = deque([0])
        for i in range(1, n):
            nums[i] = nums[dq[0]] + nums[i]
            while dq and nums[dq[-1]] <= nums[i]: dq.pop()
            dq.append(i)
            if i - dq[0] >= k: dq.popleft()
        return nums[n - 1]

# faster solution

class Solution:
    def maxResult(self, A: List[int], k: int) -> int:
        log = deque([(0, -k)])
        for i, a in enumerate(A):
            if i - log[0][1] > k:
                log.popleft()
            a += log[0][0]
            while log and log[-1][0] <= a:
                log.pop()
            log.append((a, i))
        return a
