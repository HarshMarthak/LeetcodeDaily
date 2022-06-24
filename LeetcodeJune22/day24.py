class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)
        target = [-temp for temp in target]
        heapq.heapify(target)
        while True:
            temp = -heapq.heappop(target)
            total -= temp
            if temp == 1 or total == 1: return True
            if temp < total or total == 0 or temp % total == 0:
                return False
            temp %= total
            total += temp
            heapq.heappush(target, -temp)
