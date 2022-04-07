class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        i=len(stones)-1
        while i>0:
            stones.sort()
            stones[i-1]=stones[i]-stones[i-1]
            i-=1
        return stones[0]


# better Solution

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-val for val in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x1 = heapq.heappop(stones)
            x2 = stones[0]
            if x1 != x2:
                heapq.heapreplace(stones,x1-x2)
            else:
                heapq.heappop(stones)
        if len(stones) == 0:
            return 0
        return -stones[0]        