class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target:
            return 0
        n = len(stations)
        dp = [startFuel] + [0] * n
        rst = 1000000001
        for i in range(1, n + 1):
            for j in range(i, 0, -1):
                if dp[j - 1] >= stations[i - 1][0]:
                    dp[j] = max(dp[j], dp[j - 1] + stations[i - 1][1])
                if dp[j] >= target:
                    rst = min(rst, j)
        return rst if rst != 1000000001 else -1

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        bag = []
        next_stop = startFuel
        ans = 0
        stations.append([target,0])
        for station in stations:
            while station[0] > next_stop:
                if not bag:
                    return -1
                else:
                    next_stop -= heapq.heappop(bag)
                    ans += 1
            if station[0] <= next_stop:
                heapq.heappush(bag,-1*station[1])
        return ans
